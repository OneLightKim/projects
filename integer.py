from tensorflow.core.protobuf.meta_graph_pb2 import _SIGNATUREDEF_INPUTSENTRY
import tensorflow.keras
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import cv2
import pyrebase
import json
import time
import os
#import serial

#====================파이어베이스 연결====================
#auth.json을 오픈
with open("auth.json") as f:
    ##컨피규레이션 파일을 담아두기 위해 제이슨닷로드f를 입력
    #파이어베이스에 대한 설정 파일이 담김
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()

#====================모델 가져오기====================
#Disable scientific notation for clarity
np.set_printoptions(suppress=True)
#모델 로드
model = tensorflow.keras.models.load_model('keras_model.h5')

#LABLE데이터 가져오기
f = open('labels.txt', 'r', encoding='utf-8')
labels = f.readlines()
f.close()

#====================이미지 처리====================
def preprocessing(frame):
    #이미지 뒤집기
    frame_fliped = cv2.flip(frame, 1)
    #사이즈 조정
    size = (224,224)
    frame_resized = cv2.resize(frame_fliped, size, interpolation=cv2.INTER_AREA)
    #이미지 정규화
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1
    #이미지 차원 재조정 - 예측을 위해 reshape 해줌
    frame_reshaped = frame_normalized.reshape((1,224,224,3))
    return frame_reshaped
    
def predict(data):
    prediction = model.predict(data)
    return prediction

#====================카메라 조절(영상)====================
#뒤의 0번은 연결된 카메라를 가져오기
#카메라를 제어할 수 있는 객체
capture = cv2.VideoCapture(0)

#카메라 길이 너비 조절
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)#640
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)#480

#====================데이터 처리====================
#While True : 특정 키를 누를때까지 무한 반복한다.
while True:
    #한프레임씩 읽기
    #ret : 프레임을 잘 읽었는지 여부
    #frame : 받아온 프레임
    ret, frame = capture.read()
    if ret == True:
        print("read success!")

        frame_fliped = cv2.flip(frame, 1)

        preprocessed = preprocessing(frame)
        prediction = predict(preprocessed)
        text = labels[prediction.argmax()].strip() #\n부분 제거

        #글자 출력
        font = cv2.FONT_HERSHEY_TRIPLEX
        fontScale = 1
        fontColor = (0,255,0) #R,G,B (현재는 초록색)

        #파라미터(img,text,글자위치,폰트,폰트스케일,폰트컬러)
        frame_fliped = cv2.putText(frame_fliped, text, (10,40), font, fontScale, fontColor)
        cv2.imshow("VideoFrame", frame_fliped)

        print(prediction.max())
        print(prediction.argmax())
        print(labels[prediction.argmax()])
#====================DB에 문구 올리기====================
#카메라 인식 결과에 따라 파이어베이스에 문구 올리기
        i=1
        if prediction.argmax() == 0 : #0번째 Index
            signin = {"door_status":"open", "request":"Please close the window if the fine dust level is low."}
            db.update(signin)
            cv2.imwrite('C:/teachable/open.jpg',frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
            storage.child("opena.jpg").put("open.jpg")
###photo / 
        elif prediction.argmax() == 1:
            signin = {"door_status":"open", "request":"Please close the window if the fine dust level is low and open it if it is high."}
            db.update(signin)
            cv2.imwrite('C:/teachable/open.jpg',frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
            storage.child("opena.jpg").put("open.jpg")

        else: #1번째 인덱스
            signin = {"door_status":"close", "request":"Please open the window if the fine dust level is high."}
            db.update(signin)
            cv2.imwrite('C:/teachable/close.jpg',frame, params=[cv2.IMWRITE_JPEG_QUALITY,100])
            storage.child("closea.jpg").put("close.jpg")
            
        time.sleep(1)
        if os.path.isfile('C:/teachable/close.jpg'):
            os.remove('C:/teachable/close.jpg')
        elif os.path.isfile('C:/teachable/open.jpg'):
            os.remove('C:/teachable/open.jpg')
        
        #if os.path.isfile('C:/teachable/open.jpg')
        #일정 시간(ms) 기다린 후 무한루프 종료
        #if cv2.waitkey(1) > 0:
            #break


#열려있는 모든 창 닫기
cv2.destroyAllWindows()


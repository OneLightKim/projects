#사용자의 요청을 받은 후 처리하여 응답
from django.shortcuts import render
from django.http import HttpResponse
import os #신규
import zipfile #신규
import time #신규
import shutil #zip 파일로 변경
import xml.etree.ElementTree as ET #신규
from xml.etree.ElementTree import Element, ElementTree #신규
# import aspose.words as aw #신규
import sys
import datetime

# Create your views here.
def index1(request):
    return HttpResponse('<u>Hello</u>')


def main(request):
    time = 1
    date = 2
    dt = {'data':time,'date':date}
    return render(request,'main.html',dt)

def hwpx_viewer(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
        with open(name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)
            time.sleep(1.55)
            if os.path.isfile('hwpx.hwpx') == True:  #파일 저장 여부 확인
                dialog_1 = ' 파일 이름은,'
                dialog_2 = '로 hwpx파일이 맞습니다.  잠시만 기다리시면 텍스트로 변환해드리겠습니다.'
                
                shutil.copy('hwpx.hwpx','hwpx.zip') #zip파일로 변경
                time.sleep(1.5)
                
                clear_zip = zipfile.ZipFile('./hwpx.zip') #zip파일 해제
                clear_zip.extractall('./hwpx')
                clear_zip.close()
                
                time.sleep(1.5)
            
                if os.path.isdir('hwpx') == True:
                    tree = ET.parse('./hwpx/Contents/section0.xml')
                    root = tree.getroot()
                    
                    sys.stdout = open('./static/txt/hwpx.txt','a',encoding="UTF-8")  # txt파일로 저장
                    
                    for a in root:
                        checkTag = a.tag[a.tag.find('}')+1:]
                        # print(checkTag)
                        if checkTag == 'p':
                            for b in a:
                                checkTag = b.tag[b.tag.find('}')+1:]
                                # print(checkTag)
                                if checkTag == 'linesegarray':
                                    if c is not None:
                                        print('')
                                if checkTag == 'run':
                                    for c in b:
                                        checkTag = c.tag[c.tag.find('}')+1:]
                                        # print(checkTag)
                                        if checkTag == 't':
                                            if c.text is not None:
                                                print(c.text,end='')
                                        if checkTag == 'tbl':
                                            for d in c:
                                                checkTag = d.tag[d.tag.find('}')+1:]
                                                # print(checkTag)
                                                if checkTag == 'caption':
                                                    for e in d:
                                                        checkTag = e.tag[e.tag.find('}')+1:]
                                                        # print(checkTag)
                                                if checkTag == 'tr':
                                                    print('-----------------------------------------------------------------------------------------------------------')
                                                    for f in d:
                                                        checkTag = f.tag[f.tag.find('}')+1:]
                                                        # print(checkTag)
                                                        
                                                        if checkTag == 'tc':
                                                            print('  |  ',end='')
                                                            
                                                            for g in f:
                                                                checkTag = g.tag[e.tag.find('}')+1:]
                                                                if checkTag == 'subList':
                                                                    for h in g:
                                                                        checkTag = h.tag[h.tag.find('}')+1:]
                                                                        if checkTag == 'p':
                                                                            for i in h:
                                                                                checkTag = i.tag[i.tag.find('}')+1:]
                                                                                # print(checkTag)
                                                                                
                                                                                if checkTag == 'run':
                                                                                    for j in i:
                                                                                        if j.text is not None:
                                                                                            print(j.text, end='')# checkTag = j.tag[j.tag.find('}')+1:]
                                                                                            
                                                                                if checkTag == 'linesegarray':
                                                                                    if j.text is not None:
                                                                                        print('', end='')
                                                                                        dialog_4 = '성공'
                                                    print('|',end='')
                                                    print('')                                                       
                    # return HttpResponse('%s<br>' % (dialog_4))
                return render(request, 'hwpxtxt_viewer.html')
            else:
                dialog__1 = 'hwpx 형식의 파일이 아닙니다. 뒤로 버튼을 누르고 다시 제출해주십시오'
                return HttpResponse('%s<br>' % (dialog__1))
                #upload화면으로 가는 버튼 추가
    return render(request, 'file/hwpx_viewer.html') #, context

def xlsx_viewer(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
        with open(name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)
            time.sleep(1.95)
            if os.path.isfile('xlsx.xlsx') == True:  #파일 저장 여부 확인
                dialog_1 = ' 파일 이름은,'
                dialog_2 = '로 xlsx파일이 맞습니다.  잠시만 기다리시면 텍스트로 변환해드리겠습니다.'
                
                shutil.copy('xlsx.xlsx','xlsx.zip') #zip파일로 변경
                time.sleep(1.5)
                
                clear_zip = zipfile.ZipFile('./xlsx.zip') #zip파일 해제
                clear_zip.extractall('./xlsx')
                clear_zip.close()
                
                time.sleep(1.5)
            
                if os.path.isdir('xlsx') == True:
                    tree = ET.parse('./xlsx/xl/sharedStrings.xml')
                    root = tree.getroot()
                    tmp_list= []
                    
                    for a in root:
                        checkTag = a.tag[a.tag.find('}')+1:]
                        if checkTag == 'si':
                            for b in a:
                                checkTag = b.tag[b.tag.find('}')+1:]
                                if b.text is not None:
                                    tmp_list.append(b.text)  
                                    dialog_4 = '텍스트'
                    ## tmp_v에 sharedStrings 텍스트들 인덱스 넣기
                    tree = ET.parse('./xlsx/xl/worksheets/sheet1.xml')
                    root = tree.getroot()
                    tmp_v = []
                    for a in root:
                        checkTag = a.tag[a.tag.find('}')+1:]
                        # print(checkTag)
                        if checkTag == 'sheetData':
                            for b in a:
                                checkTag = b.tag[b.tag.find('}')+1:]
                                # print(checkTag)
                                if checkTag == 'row':
                                    for c in b:
                                        checkTag = c.tag[c.tag.find('}')+1:]
                                        if checkTag == 'c':
                                            for d in c:
                                                checkTag = d.tag[d.tag.find('}')+1:]
                                            # print(c.attrib)
                                            c_s = c.get('t')
                                            if c_s == 's':
                                                if checkTag == 'v':
                                                    tmp_v.append(int(d.text))
                    ## tmp_v 인덱스 중복 제거
                    result = [] # 중복 제거된 값들이 들어갈 리스트
                    for value in tmp_v:
                        if value not in result:
                            result.append(value)
                    tmp_v = result
                    
                    #출력
                    count=0
                    sys.stdout = open('./static/txt/xlsx.txt','a', encoding="UTF-8")
                    for i in tmp_v:
                        try:
                            # 23줄 이상인 요소는 한줄을 사용
                            if len(tmp_list[i])>23:
                                print('\n',tmp_list[i])
                                count +=1
                            # 다른 요소는 띄어쓰기4번으로 구분
                            else:
                                print(tmp_list[i],end='')
                                print('    ', end='')
                                count +=1
                        except:
                            pass     
                    # print('\n',count)
                    dialog_5 = '인덱스'                  

                    # return HttpResponse('%s<br>%s' % (dialog_4, dialog_5))
                return render(request, 'xlsxtxt_viewer.html')

            else:
                dialog__1 = 'xlsx 형식의 파일이 아닙니다. 뒤로 버튼을 누르고 다시 제출해주십시오'
                return HttpResponse('%s<br>' % (dialog__1))
                #upload화면으로 가는 버튼 추가
                
    return render(request, 'file/xlsx_viewer.html')

def pptx_viewer(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
        with open(name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)
            time.sleep(1.55)
            if os.path.isfile('pptx.pptx') == True:  #파일 저장 여부 확인
                dialog_1 = ' 파일 이름은,'
                dialog_2 = '로 pptx파일이 맞습니다.  잠시만 기다리시면 텍스트로 변환해드리겠습니다.'
                
                shutil.copy('pptx.pptx','pptx.zip') #zip파일로 변경
                time.sleep(1.5)
                
                clear_zip = zipfile.ZipFile('./pptx.zip') #zip파일 해제
                clear_zip.extractall('./pptx')
                clear_zip.close()
                
                time.sleep(1.5)
            
                if os.path.isdir('pptx') == True:
                    tree = ET.parse('./pptx/ppt/slides/slide1.xml')
                    root = tree.getroot()
                    #ppt slide1.xml의 도형 텍스트 추출
                    
                    for a in root:
                        checkTag = a.tag[a.tag.find('}')+1:]
                        # print(checkTag)
                        if checkTag == "cSld":
                            for b in a:
                                checkTag = b.tag[b.tag.find('}')+1:]
                                # print(checkTag)
                                if checkTag == "spTree":
                                    for c in b:
                                        checkTag = c.tag[c.tag.find('}')+1:]
                                        # print(checkTag)
                                        if checkTag == "sp":
                                            for d in c:
                                                checkTag = d.tag[d.tag.find('}')+1:]
                                                # print(checkTag)
                                                if checkTag == "txBody":
                                                    for e in d:
                                                        checkTag = e.tag[e.tag.find('}')+1:]
                                                        # print(checkTag)
                                                        if checkTag == "p":
                                                            for f in e:
                                                                checkTag = f.tag[f.tag.find('}')+1:]
                                                                # print(checkTag)
                                                                if checkTag == "r":
                                                                    sys.stdout = open('./static/txt/pptx.txt','a',encoding="UTF-8")
                                                                    for g in f:
                                                                        checkTag = g.tag[g.tag.find('}')+1:]
                                                                        # print(checkTag)
                                                                        if checkTag == "t":
                                                                            print(g.text)
                                                                            dialog_4 = '성공'                                                        
                    # return HttpResponse('%s<br>' % (dialog_4))
                return render(request, 'pptxtxt_viewer.html')

            else:
                dialog__1 = 'pptx 형식의 파일이 아닙니다. 뒤로 버튼을 누르고  다시 제출해주십시오'
                return HttpResponse('%s<br>' % (dialog__1))
                #upload화면으로 가는 버튼 추가
                
    return render(request, 'file/pptx_viewer.html')

def pdf_viewer(request):
    if request.method == 'POST':
        # upload_file = request.FILES.get('file') # 파일 객체
        # name = upload_file.name # 파일 이름
        # size = upload_file.size # 파일 크기
        # with open(name, 'wb') as file: # 파일 저장
        #     for chunk in upload_file.chunks():
        #         file.write(chunk)
        #     time.sleep(1.55)
    # if request.method == 'POST':
    #     upload_file = request.FILES.get('file') # 파일 객체
    #     suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    #     fileName = suffix + '.pdf'
    #     name = request.FILES['filename'].name #upload_file.fileName # 파일 이름
    #     # size = upload_file.size # 파일 크기
    #     with open(name, 'wb') as file: # 파일 저장
    #         for chunk in upload_file.chunks():
    #             file.write(chunk)
            # time.sleep(10.55)
            # if os.path.isfile('pdfpdf.pdf') == True:  #파일 저장 여부 확인
        dialog_1 = ' 파일 이름은,'
        dialog_2 = '로 pdf파일이 맞습니다. 잠시만 기다리시면 텍스트로 변환해드리겠습니다.'
        # (요청이 온 시간 datetime stringfy_)(파일)
        # time.sleep(300.5)
        
        # pdf = aw.Document("pdfpdf.pdf")
        # time.sleep(10.566)
        # pdf.save("pdf_text.txt")
        # dialog_3 = '저장 성공'
        # time.sleep(10.566)
        return render(request, 'pdftxt_viewer.html')
                
                # return HttpResponse('%s<br>%s%s' % (dialog_1, name, dialog_2))

            # else:
            #     dialog__1 = 'pdf 형식의 파일이 아닙니다. 뒤로 버튼을 누르고 다시 제출해주십시오'
            #     return HttpResponse('%s<br>' % (dialog__1))
            #     # upload화면으로 가는 버튼 추가
                
    return render(request, 'file/pdf_viewer.html')

def file_viewer(request):
    a={}
    # count = 0
    # f = open("./viewer/extracted-text-pdf.txt",'rt', encoding="UTF8")
    # while True:
    #     line = f.readline()
    #     if not line: break
    #     a[count]=line
    #     count +=1
    # f.close()
    return render(request, 'file_viewer.html',a)

def test(request):
    return render(request, 'test.html')
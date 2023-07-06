#include "LiquidCrystal_I2C.h"
#include "emotion.h"
#include "PMsensor.h"
#include "TB6612FNG.h"
#include <WiFi.h>
#include <IOXhop_FirebaseESP32.h>                                             // firebase library
#include <Stepper.h>

#define FIREBASE_HOST "project2-c6dd2-default-rtdb.firebaseio.com/"                         // the project name address from firebase id
#define FIREBASE_AUTH "0YD0zLKXoqtvb5WCPhm3dEk7zjfjIo501ICgpktI"                    // the secret key generated from firebase
#define WIFI_SSID "kimkwangil"                                          // input your home or public wifi name 
#define WIFI_PASSWORD "76493588"  

#define sensitivity  0.1  //먼지 센서의 민감도 수치
//민감도의 숫자가 클 경우 : 센서 값의 변화가 민감함
//민감도의 숫자가 작을 경우 : 센서 값의 변화가 둔함

int stepsPerRev = 250
; // 한바퀴(360): 2048, 반 바퀴(180) : 1024
Stepper stepper (stepsPerRev, 19, 18, 17, 16);

Tb6612fng motor(15, 2, 0, 4);
const int sensorPin = 33;
const int sensorLED = 32;

PMsensor PM;
LiquidCrystal_I2C lcd(0x27, 16, 2);
//LCD 이름 : 0x27 또는 0x3F 입력
String doorStatus = ""; 
String doorChange = ""; 
String fireStatus = ""; 

void setEmoticon(float data) {  
  if (data > 30) {                                 //Good. data < 30, Green LED, Motor stop

    lcd.createChar(4,
    topAngry1);
    lcd.createChar(5, topAngry2);
    lcd.createChar(6, bottomAngry1);
    lcd.createChar(7, bottomAngry2);
    digitalWrite(27, HIGH);
    digitalWrite(26, LOW);
    digitalWrite(25, LOW);
     motor.drive(0.5, 3500);



  }
  else if (data > 10) {                           //Normal. 30 < data < 80, Yellow LED, Motor start

    lcd.createChar(4, topSoSo1);
    lcd.createChar(5, topSoSo2);
    lcd.createChar(6, bottomSoSo1);
    lcd.createChar(7, bottomSoSo2);
    digitalWrite(27, HIGH);
    digitalWrite(26, HIGH);
    digitalWrite(25, LOW);
     motor.drive(0.5, 3500);




  }
  else {                                                    //Worst. 80 < data, Red LED, Motor Max

    lcd.createChar(4, topSmile1);
    lcd.createChar(5, topSmile2);
    lcd.createChar(6, bottomSmile1);
    lcd.createChar(7, bottomSmile2);
    digitalWrite(27, LOW);
    digitalWrite(26, HIGH);
    digitalWrite(25, LOW);
    motor.brake();
 
  }
}



void setup() {

  lcd.init();
  lcd.backlight();
  lcd.createChar(2, dust);
  motor.begin();
  
  pinMode(27, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(0, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(15, OUTPUT);
  digitalWrite(15, OUTPUT);
  pinMode(16, OUTPUT);
  pinMode(17, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  Serial.begin(115200);
  stepper.setSpeed(10);

  /////(infrared LED pin, sensor pin)  /////
  PM.init(sensorLED, sensorPin);
 WiFi.begin(WIFI_SSID, WIFI_PASSWORD);                                      //try to connect with wifi

  Serial.print("Connecting to ");

  Serial.print(WIFI_SSID);

  while (WiFi.status() != WL_CONNECTED) {

    Serial.print(".");

    delay(500);
  }
    Serial.println();

  Serial.print("Connected to ");

  Serial.println(WIFI_SSID);

  Serial.print("IP Address is : ");

  Serial.println(WiFi.localIP());                                                      //print local IP address

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);                                       // connect to firebase

  Firebase.setString("Power", "OFF");     
}

int value = 0;

void loop() {

   fireStatus = Firebase.getString("Power"); 
   doorStatus = Firebase.getString("door_status");
   doorChange = Firebase.getString("door_change");
   while(fireStatus == "ON"){
    
           float data = 0;
           int err = PMsensorErrSuccess;
            if ((err = PM.read(&data, true, sensitivity)) != PMsensorErrSuccess) {
             Serial.print("data Error = ");
             Serial.println(err);
             delay(1500);
           }
           
           Serial.println(data);
           delay(1500);
           setEmoticon(data);

           int a = int(data);
           String str = String(a);
           Firebase.setString("pm",str);
           lcd.setCursor(0, 0);
           lcd.write(2);
           lcd.print(" ");
           lcd.print(data);

           if (data > 100) {
              lcd.print("ug");
           }
           else if (data > 10) {
              lcd.print(" ug");
           }
           else {
             lcd.print(" ug  ");
            }
           lcd.setCursor(2, 1);
           if (data > 80) {
              lcd.print("bad ");
             
           }
           else if (data > 30) {
              lcd.print("soso");

           }
           else {
             lcd.print("good");

            }            
  
            lcd.setCursor(13, 0);
            lcd.write(4);
            lcd.write(5);

            lcd.setCursor(13, 1);
            lcd.write(6);
            lcd.write(7);
            doorStatus = Firebase.getString("door_status");

            while(doorStatus == "open")
            {
              doorChange = Firebase.getString("door_change");
              if(doorChange=="close")
              {
                stepper.setSpeed(8);
                stepper.step(stepsPerRev);
                doorStatus = Firebase.getString("door_status");
                if(doorStatus=="close"){break;}
                }

                }
            
            doorStatus = Firebase.getString("door_status");
            while(doorStatus == "close"){
              doorChange = Firebase.getString("door_change");
              if(doorChange=="open"){
                stepper.setSpeed(8);
                stepper.step(-stepsPerRev);
                doorStatus = Firebase.getString("door_status");
                if(doorStatus=="open"){break;}
                }
                }
            fireStatus = Firebase.getString("Power");
            if (fireStatus == "OFF"){
                digitalWrite(27, LOW);
                digitalWrite(26, LOW);
                digitalWrite(25, LOW);
                lcd.setCursor(0,0);
                lcd.print("end             ");
                lcd.setCursor(0,1);
                lcd.print("                ");
                motor.brake();
                break;
            }
            
   }
            }

         

// 라이브러리
// currentPosition() //현재 위치 값
// move(distance)  //이동할 거리 지정
// stepper.setCurrentPosition(position); //현재 스탭을 설정
// stepper.currentPosition(); //현재 스탭을 반환
// stepper.setAcceleration(2000); //가속량을 설정함
// stepper.moveTo(1000); //목표스탭량을 설정함
// stepper.runToPosition(); //가속도 조절 스탭모터제어

#include <AccelStepper.h>

#define moterInterfaceType 1 // 스텝모터의 인터페이스 타입을 나타내는 상수
#define sensorA 3 // 적외선센서
#define enablePin 4 //스텝모터(전원해제핀)
#define dirxPin 5 // 스텝모터
#define stepxPin 6 // 스텝모터
#define sensorB 7 // 적외선센서

AccelStepper stepperx = AccelStepper(moterInterfaceType, stepxPin, dirxPin);
// AccelStepper stepperx = AcclStepper(연결방식, step핀, dir핀)

int state1; // 센서 상태 저장 변수
int state2; // 센서 상태 저장 변수
int isStop = 0; // 스텝모터 중지 결정 변수


void setup() {   
  pinMode(enablePin, OUTPUT); // 모터는 OUTPUT
  pinMode(sensorA, INPUT); // 센서는 INPUT
  pinMode(sensorB, INPUT);
  digitalWrite(enablePin, LOW); 
  stepperx.setMaxSpeed(1000); // 최대속도
  stepperx.setSpeed(900);
  Serial.begin(9600);

}

void loop() {

  state1 = digitalRead(sensorA); // 적외선 센서를 읽어와 저장
  state2 = digitalRead(sensorB);

  if (!isStop) // 센서가 멈추지 않을 경우
  {
    if (state1 == LOW) { //센서가 감지되면 
      isStop = 1; // 동작을 멈춤
      Serial.print("sensor1=");
      String s = Serial.readString(); // 문자열을 읽어와 'test'에 저장
      Serial.println(s);    
    }

    else if(state2 == LOW){
      isStop = 1; // 동작을 멈춤
      Serial.print("sensor2=");
      String s = Serial.readString(); // 문자열을 읽어와 'test'에 저장
      Serial.println(s);
    }

    else { // 센서가 감지되지 않으면
      stepperx.setSpeed(900); // 설정된 속도와 방향
      stepperx.runSpeed(); // 스텝 모터를 움직임
    }  
  }     


  if (Serial.available() > 0)  // 0 이상의 시리얼통신이 들어올 경우
  {
    Serial.print("input=");
    String test = Serial.readString(); // 문자열을 읽어와 'test'에 저장
    Serial.println(test);

    isStop = 0; // 동작을 시작

    int i = 0;
    for(i = 0; i < 10000; i++) 
    {
      stepperx.setSpeed(900);
      stepperx.runSpeed();
    }
  }
}

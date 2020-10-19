#include <Servo.h> 
#include <Stepper.h>
int trigPin = 11;    // Trigger
int echoPin = 12;    // Echo
long duration, cm, inches;
int servoPin = 9;
char serialData;
Servo servo;  
Servo servo2;
Servo servo3;
Servo servoGame;
int motorPin = 10;
const int speed =180;
const int stepsPerRevolution = 2048;
Stepper myStepper = Stepper(stepsPerRevolution, 8, 6, 7, 5);
int angle = 0;



void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorPin, OUTPUT);
  servo.attach(servoPin); 
  servo2.attach(4);
  servo3.attach(3);
  servoGame.attach(13);
  servo.write(30);
  servo2.write(30);
  servo3.write(0);
  
  servoGame.write(30);
  myStepper.setSpeed(16);
  

//  
 
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  
  // Convert the time into a distance
  cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
  inches = (duration/2) / 74; 

  if (inches>=4 && inches<=6){
    Serial.println("playSong");
    
  }


  // put your main code here, to run repeatedly:
  if (Serial.available()>0){ 
    serialData = Serial.read();
    if (serialData=='1'){
      for(angle = 30; angle < 270; angle++)  
      {                                  
        servo.write(angle);               
        delay(1);              
      } 
      
    }
    if (serialData=='2'){
      for(angle = 270; angle > 30; angle--)  
      {                                  
        servo.write(angle);               
        delay(1);              
      } 
      digitalWrite(motorPin, LOW);  
    }
    if (serialData=='3'){
      //deal with Stepper
      myStepper.step(3248);
      
    }
    if (serialData=='4'){
      //deal with Stop Stepper
      myStepper.step(3248);
    }
    if (serialData=='5'){
      //deal with Servo 5
       myStepper.step(860);
      
    }
    if (serialData=='6'){
      //deal with Servo 6
       myStepper.step(860);
    }
     if (serialData=='7'){
      //deal with TREAT Latch
      for(angle = 30; angle < 270; angle++)  
        {                                  
        servo2.write(angle);               
        delay(1);              
        } 
        delay(300);
        servo2.write(30);
        delay(3000);
        //start conveyor
        digitalWrite(motorPin, speed);
        
    }
     if (serialData=='8'){
      //deal with TREAT Latch
      for(angle = 30; angle < 270; angle++)  
        {                                  
        servo3.write(angle);               
        delay(1);              
        } 
        delay(300);
        servo3.write(30);
    }
    if (serialData=='r'){
      Serial.flush();
      servo.write(0);    
      
    }
    
  }
  
}

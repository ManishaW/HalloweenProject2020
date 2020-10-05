#include <Servo.h> 
int trigPin = 11;    // Trigger
int echoPin = 12;    // Echo
long duration, cm, inches;
int servoPin = 9;
char serialData;
Servo servo;  
 
int angle = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  servo.attach(servoPin); 
  servo.write(30);
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
  if (inches<6 && inches>0){
    Serial.println("playSong");
  }
 
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    serialData = Serial.read();
    Serial.print(serialData);  
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
    }
    if (serialData=='3'){
      //deal with Servo 3
    }
    if (serialData=='4'){
      //deal with Servo 4
    }
    if (serialData=='5'){
      //deal with Servo 5
    }
    
  }
  
}

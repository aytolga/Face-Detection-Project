
#include "cvzone.h"    
#include "Servo.h"    //Implementatin of some neccessary libraries.
Servo servo;          //Definiton of servo motor.               
SerialData data(2,3); // To create the serial object to recieve some values from Python.                       
int value[10];        // An array for stored values.
int light = 10;
void setup () {
  
  data.begin(9600); 
  servo.attach(9);      //In the setup side servo is attached in pin 10 and LED is attached pin 10.
  pinMode(light,OUTPUT);
}

void loop () {
  data.Get(value);     //Starting to getting values from Python    
  servo.write(value[0]);  //Servo motor commands  
  delay(0);
  digitalWrite(light,value[0]); //LED commands
  delay(0);
  
}

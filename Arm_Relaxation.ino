#include <Servo.h> 
Servo myservo;   
int pos = 0;     
void setup() { 
    myservo.attach(9);   
} 
void loop() { 
    if(pos = 180) 
    {   
        myservo.write(pos);               
        delay(15);                       
    } 
    else           
    {
        myservo.write(pos);               
        delay(15); 
    } 
} 
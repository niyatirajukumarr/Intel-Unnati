#include <Servo.h> 
Servo myservo;        
int pos = 0;                
void setup() { 
    // create servo object to control a servo 
    // twelve servo objects can be created on most boards 
    // variable to store the servo position 
    myservo.attach(9);   // attaches the servo on pin 9 to the servo object 
} 
void loop() { 
    for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees 
    myservo.write(pos);                      
    delay(15);                                    
    } 
    // in steps of 1 degree 
    // tell servo to go to position in variable 'pos' 
    // waits 15 ms for the servo to reach the position 
    for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees 
    myservo.write(pos);    
    delay(15);                    
    }
}
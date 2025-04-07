#include <Servo.h>

Servo redServo;
Servo greenServo;
Servo blueServo;

void setup() {
  Serial.begin(9600);
  redServo.attach(3);
  greenServo.attach(5);
  blueServo.attach(6);
}

void loop() {
  if (Serial.available()) {
    char color = Serial.read();

    switch (color) {
      case 'R':
        redServo.write(90);   // Move to drop red object
        delay(1000);
        redServo.write(0);    // Return to default
        break;

      case 'G':
        greenServo.write(90);
        delay(1000);
        greenServo.write(0);
        break;

      case 'B':
        blueServo.write(90);
        delay(1000);
        blueServo.write(0);
        break;

      default:
        // No action
        break;
    }
  }
}
#define BLYNK_TEMPLATE_ID "TMPL2rwFCBE0s"
#define BLYNK_TEMPLATE_NAME "Test1"
#define BLYNK_AUTH_TOKEN "DRqlWX25YznvYkOvUgNGGUX_xRKtSM5F"

#include <WiFi.h>// "Connecting ESP32 to Wi-Fi" library
#include <BlynkSimpleEsp32.h> // "Connecting ESP32 to BLYNK" library
#include <ESP32Servo.h>

// WiFi credentials
char ssid[] = "Mohamed's Galaxy M31";
char pass[] = "drwu2522";
// char ssid[] = "Orange-VGHS";
// char pass[] = "whitecheese905";
char auth[] = BLYNK_AUTH_TOKEN;

// Buzzer on GPIO 26
#define PIR_PIN 14
#define BUZZER_PIN 26
#define SERVO_PIN 27


Servo myServo;
int servoAngle = 0;       // Initial angle: Door is CLOSED (0°)
bool motionDetected = false;

void setup() {
  Serial.begin(115200);
  
  // Setup buzzer pin
  pinMode(PIR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW); // Start with buzzer OFF

  //Setup servo
  myServo.attach(SERVO_PIN);
  myServo.write(servoAngle);  // Set initial door position


  Blynk.begin(auth, ssid, pass); // Start BLYNK connection
  
  Serial.println("ESP32 ready! Buzzer on GPIO 26");
}

void loop() {
  Blynk.run(); // Start Blynk running
  int pirValue = digitalRead(PIR_PIN);

  if (pirValue == HIGH && !motionDetected) {
    motionDetected = true;

    // Beep the buzzer briefly
    digitalWrite(BUZZER_PIN, HIGH);
    delay(300);
    digitalWrite(BUZZER_PIN, LOW);

    // Toggle door state based on current servoAngle
    if (servoAngle > 0) {
      servoAngle = 0;
      Serial.println("Motion Detected → Door is CLOSING (0°)");}
      myServo.write(servoAngle);
      delay(500);  // Allow servo to move
      Blynk.virtualWrite(V26, 0);
  }

  if (pirValue == LOW) {
    motionDetected = false;  // Reset flag for next motion detection
  }

}

// Control buzzer with Virtual Pin V26
BLYNK_WRITE(V26) {
  int switch_button = param.asInt(); // Get value from app (0 or 1)
  
  if(switch_button == 0){ // door should be closed
      if (servoAngle > 0) { // door was found open
        servoAngle = 0; // close door
        myServo.write(servoAngle); // set the servo motor's angle to 0
        delay(500);
    }
  }

  if(switch_button == 1){ //door should be open
    if (servoAngle == 0) { // if door was found closed
        servoAngle = 90; // open door
        myServo.write(servoAngle); // set servo motor's angle to 90
        delay(500);  // Allow servo to move
    }
  }


}

#include <Ultrasonic.h>

Ultrasonic ultrasonic(5, 6);
int LED = 2;
int threshold = 100;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int distance = ultrasonic.distanceRead();
  if(distance< threshold)
  {
  digitalWrite(LED, HIGH);
  Serial.println("HIGH");
  delay(10000);
  }
  else{
  digitalWrite(LED,LOW);
  }
  delay(1000);
  
}

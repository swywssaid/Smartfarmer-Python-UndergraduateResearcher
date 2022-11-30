int cds = A0;

void setup() {
    Serial.begin(9600);
    Serial.println("start");
}

void loop() {
  int cdsValue = analogRead(cds);
  Serial.println(cdsValue);
  delay(1800000);
}

#include <cm1106_i2c.h>

CM1106_I2C cm1106_i2c;

// #define CM1107

void setup() {
  cm1106_i2c.begin();
  Serial.begin(9600);
  delay(1000);
  }

void loop() {
  uint8_t ret = cm1106_i2c.measure_result();

  if (ret == 0) {
    Serial.print("Co2 : ");
    Serial.println(cm1106_i2c.co2);
  }
  delay(1000);
}

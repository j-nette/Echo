#include <Arduino.h>
#include <Wire.h>
#include <SPI.h>

#include "LCD5110_Graph.h"

LCD5110 display(8,9,10,12,11);

extern uint8_t SmallFont[];

void setup(){
    display.InitLCD();
    display.clrScr();
    display.setFont(SmallFont);

    Serial.begin(9600);
    delay(2000);

    int roll = 4;
    display.print((String) "You rolled a" + roll, CENTER, 20);
    display.print((String) roll, CENTER, 30);

    Serial.println("Roll:" + roll);
    Serial.println("1");
}


void main(){
}


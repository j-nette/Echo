#include <Arduino.h>
#include <Wire.h>
#include <SPI.h>

#include <LCD5110_Graph.h>

LCD5110 display(8,9,10,12,11);

extern uint8_t SmallFont[];
//extern uint8_t TinyFont[];

extern uint8_t Load[];

void startUp();
void loading();
void rollDie(int roll);
void getAction(int action, int data);

void setup(){
  display.InitLCD();
  display.clrScr();
  display.setFont(SmallFont);

  Serial.begin(9600);
  startUp();
  delay(500); // delay to make sure everything booted properly
}

void loop(){
   if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n');
    int commaPos = inputString.indexOf(',');
    
    if (commaPos != -1) {
      String actionString = inputString.substring(0, commaPos);
      String dataString = inputString.substring(commaPos + 1);
      
      int action = actionString.toInt();
      int data = dataString.toInt();

      Serial.println(action);
      Serial.println(data);

      getAction(action, data); 
    }
  }
}

void getAction(int action, int data){
  if(action == 1){ // roll a die
    rollDie(data);
  }
}


void startUp(){
  display.clrScr();
  display.setFont(SmallFont);

  display.print((String) "Echo", CENTER, 5);
  display.print((String) "Your Friendly", CENTER, 20);
  display.print((String) "Assistant", CENTER, 30);

  display.update();
}

void loading(){
  display.clrScr();
  int x = 20;
  for (int count = 0; count < 3; count++) {
    delay(1000);
    display.drawBitmap(x, 20, Load, 5, 5);
    display.update();
    x += 20;
  }
  display.clrScr();
}

void rollDie(int roll){
  loading();

  display.print((String) "You rolled a", CENTER, 20);
  display.print((String) roll, CENTER, 30);

  Serial.println("1"); //Telling the python script that the command is done
}
#include<Servo.h>
#include <LiquidCrystal.h>
Servo servo1;
Servo servo2;

int cont=0;

int led1=10;
int luz=A0;
int ref=A1;

int luz1=0;
int ref1=0;

int sensor_ent=2;
int sensor_sal=4;
int pulsa_ent=3;
int pulsa_sal=5;
int var=0;
int var1=0;
int var2=0;
int var3=0;

int rojo=8;
int amarillo=9;
int verde=11;


void setup() {
pinMode(led1, OUTPUT);
pinMode(rojo, OUTPUT);
pinMode(amarillo, OUTPUT);
pinMode(verde, OUTPUT);

pinMode(sensor_ent,INPUT);
pinMode(pulsa_ent,INPUT);
pinMode(sensor_sal,INPUT);
pinMode(pulsa_sal,INPUT);

servo1.attach(7);
servo2.attach(13);
}

void loop() {
luz1=analogRead(luz);
ref1=analogRead(ref);
var= digitalRead(sensor_ent);
var1=digitalRead(sensor_sal);
var2=digitalRead(pulsa_ent);
var3=digitalRead(pulsa_sal);

if (luz1<ref1){
  digitalWrite(led1,HIGH);
}  else
  digitalWrite(led1,LOW);


if (var==true && var2==true) {
  cont ++;
  servo1.write(90);
}
if (var==false && var2==true) {
  servo1.write(0);
}
 
if (var1==true && var3==true) {
  cont --;
  servo2.write(90);
}
  if (var1==false && var3==true) {
  servo2.write(0);
}

if (cont>100) {
  digitalWrite(rojo,LOW);
  digitalWrite(amarillo,HIGH);
  digitalWrite(verde,HIGH);
}
if (cont>=90 && cont<100) {
  digitalWrite(amarillo,LOW);
  digitalWrite(rojo, HIGH);
  digitalWrite(verde,HIGH);
}
 if (cont<90) {
 digitalWrite(verde,LOW);
 digitalWrite(rojo,HIGH);
 digitalWrite(amarillo, HIGH);
 }
}
 


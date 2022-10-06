#define ENABLE 5
#define DIRECTION 6

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// RADIO
RF24 radio(7, 8); // CE, CSN
const byte numSlaves = 3;
const byte slaveAddress[numSlaves][6] = {"00002", "00003", "00004"};

// ENCODER
volatile long temp, counter = 0;
long aux = 0;
void ai0() {
  if (digitalRead(3) == LOW) {
    counter++;
  } else {
    counter--;
  }
}
void ai1() {
  if (digitalRead(2) == LOW) {
    counter--;
  } else {
    counter++;
  }
}


void setup() {
  // SERIAL
  Serial.begin (9600);
  // ENCODER
  pinMode(2, INPUT_PULLUP); // internal pullup input pin 2
  pinMode(3, INPUT_PULLUP); // internal pullup input pin 3
  attachInterrupt(0, ai0, RISING);
  attachInterrupt(1, ai1, RISING);
  // RELES
  pinMode(ENABLE, OUTPUT); //RELE ENABLE
  pinMode(DIRECTION, OUTPUT); //RELE DIRECAO
  digitalWrite(ENABLE, LOW);
  // RADIO
  radio.begin();
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

// CONTROLE ENCODER + RELES
void TurnLeft(int step)
{
  digitalWrite(ENABLE, HIGH);
  digitalWrite(DIRECTION, LOW);
  counter = 0;
  while (counter >= step)
  {
    if ( counter != temp)
    {
      Serial.print("CONTADOR");
      Serial.println(counter);
      temp = counter;
      if (temp <= step)
      {
        digitalWrite(ENABLE, LOW);  //desaciona relé de controle, motor não gira mais
        aux = 0;
        counter = 0;
        return;
      }
    }
  }
}
void TurnRight(int step)
{
  digitalWrite(ENABLE, HIGH);
  digitalWrite(DIRECTION, HIGH);
  counter = 0;
  while (counter <= step)
  {
    if ( counter != temp)
    {
      Serial.print("CONTADOR:");
      Serial.println(counter);
      temp = counter;
      if (temp >= step)
      {
        digitalWrite(ENABLE, LOW);  //desaciona relé de controle, motor não gira mais
        aux = 0;
        counter = 0;
        return;
      }
    }
  }
}


void loop() {
  // MENU INICIAL
  Serial.print("Selecione o motor a mover\n");

  while (Serial.available() == 0) {} //ESPERA
  int n = Serial.parseInt();

  // MOTOR 1 (MESTRE)
  if (n == 1) {
    Serial.print("Digite o numero de passos\n");
    while (Serial.available() == 0) {} //ESPERA
    aux = Serial.parseInt();
    if (aux < 0)
      TurnLeft(aux);

    else if (aux > 0)
      TurnRight(aux);

    else if (aux == 0)
      digitalWrite(ENABLE, LOW);
  }
  // MOTOR 2
  if (n == 2) {
    Serial.print("Digite o numero de passos\n");
    while (Serial.available() == 0) {} //ESPERA
    aux = Serial.parseInt();
    radio.openWritingPipe(slaveAddress[0]);
    radio.write(&aux, sizeof(aux));
  }
  // MOTOR 3
  if (n == 3) {
    Serial.print("Digite o numero de passos\n");
    while (Serial.available() == 0) {} //ESPERA
    aux = Serial.parseInt();
    radio.openWritingPipe(slaveAddress[1]);
    radio.write(&aux, sizeof(aux));
  }
  // MOTOR 4
  if (n == 4) {
    Serial.print("Digite o numero de passos\n");
    while (Serial.available() == 0) {} //ESPERA
    aux = Serial.parseInt();
    radio.openWritingPipe(slaveAddress[2]);
    radio.write(&aux, sizeof(aux));
  }



}

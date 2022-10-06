#define ENABLE 5
#define DIRECTION 6

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00003";
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
  Serial.begin (57600);
  pinMode(2, INPUT_PULLUP); // internal pullup input pin 2
  pinMode(3, INPUT_PULLUP); // internal pullup input pin 3
  pinMode(ENABLE, OUTPUT); //RELE ENABLE
  pinMode(DIRECTION, OUTPUT); //RELE DIRECAO
  digitalWrite(ENABLE, LOW);
  attachInterrupt(0, ai0, RISING);
  attachInterrupt(1, ai1, RISING);

  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}

void TurnLeft(int step)
{
  counter = 0;
  digitalWrite(DIRECTION, LOW);
  digitalWrite(ENABLE, HIGH);
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
  counter = 0;
  digitalWrite(ENABLE, HIGH);   //aciona o relé de direção, motor girando para esquerda
  digitalWrite(DIRECTION, HIGH); //desaaciona o relé de direção, motor girando para direita
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


  if (radio.available()) {
    radio.read(&aux, sizeof(aux));
  }

  if (aux != 0) {
    Serial.print("aux:");
    Serial.print(aux);
    Serial.print("\n");
    delay(1000);
  }
  else
    digitalWrite(ENABLE, LOW);

  if (aux > 0)
    TurnRight(aux);

  if (aux < 0)
    TurnLeft(aux);
}

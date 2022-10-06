#define ENABLE 5
#define DIRECTION 6

volatile long temp, counter = 0; //This variable will increase or decrease depending on the rotation of encoder
int aux = 0;

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
  Serial.begin (9600);
  pinMode(2, INPUT_PULLUP); // internal pullup input pin 2
  pinMode(3, INPUT_PULLUP); // internal pullup input pin 3
  pinMode(ENABLE, OUTPUT); //RELE ENABLE
  pinMode(DIRECTION, OUTPUT); //RELE DIRECAO
  digitalWrite(ENABLE, LOW);
  attachInterrupt(0, ai0, RISING);
  attachInterrupt(1, ai1, RISING);
}

void TurnLeft(int step)
{
  counter = 0;
//  digitalWrite(DIRECTION, HIGH);  //aciona o relé de direção, motor girando para esquerda
//  digitalWrite(ENABLE, HIGH);     //aciona o relé de controle, motor começa a girar
  Serial.print("PASSO:");
  Serial.print(step);
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
//  digitalWrite(ENABLE, HIGH);   //aciona o relé de direção, motor girando para esquerda
//  digitalWrite(DIRECTION, LOW); //desaaciona o relé de direção, motor girando para direita
  Serial.print("PASSO:");
  Serial.print(step);
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

  while (Serial.available() == 0){}
      aux = Serial.parseInt();
    
    if (aux > 0)
    { // VALOR POSITIVO SOLTA
      digitalWrite(ENABLE, HIGH);  
      digitalWrite(DIRECTION, LOW);
      TurnRight(aux);
      digitalWrite(ENABLE, LOW);
    }
    
    if (aux <0) { // VALOR NEGATIVO PUXA
      digitalWrite(ENABLE, HIGH);  
      digitalWrite(DIRECTION, HIGH);
      TurnLeft(aux);
      digitalWrite(ENABLE, LOW);
    }

}

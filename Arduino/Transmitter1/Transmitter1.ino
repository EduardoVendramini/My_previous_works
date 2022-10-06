#define ENABLE 5
#define DIRECTION 6
#include <EEPROM.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <math.h>




// CALCULOS
//TODAS AS UNIDADES ESTÃO EM MILIMETROS//
int mmToStep = 25;   //RAZÃO ENTRE PASSOS E mm DO FIO
//PONTO INICIAL QUE ENCONTRAMOS A CARGA CENTRAL
int   x0 = 3750;   //x inicial
int   y0 = 3000;   //y inicial
//PONTO EM QUE QUEREMOS QUE A CARGA FINAL CHEGUE
int xf;    //x final
int yf;    //y final
//PONTOS EM RELAÇÃO A CADA "POSTE" OU ENCODER
int   xa0 = 7580;  // (MOTOR 1)
int   ya0 = 6010;  // (MOTOR 1)
int   xb0 = -330;  // (MOTOR 2)
int   yb0 = 6010;  // (MOTOR 2)
int   xc0 = 0;     // (MOTOR 3)
int   yc0 = 0;     // (MOTOR 3)
int   xd0 = 7580;  // (MOTOR 4)
int   yd0 = 0;     // (MOTOR 4)
//VARIAVEIS QUE VÃO RECEBER A VARIAÇÃO DA DIST. DO FIO
long distances[3];
float cableDist(int xp0, int yp0, int x0, int y0, int xf, int yf) { // parâmetros -> xa0, ya0, x0, y0, xf, yf
  float dist;
  dist = sqrt( pow((xf - xp0), 2) + pow((yf - yp0), 2))   -  (   sqrt( pow((x0 - xp0), 2) + pow((y0 - yp0), 2) )   );
  return dist * mmToStep;
}



// RADIO
RF24 radio(7, 8); // CE, CSN
const byte numSlaves = 3;
const byte slaveAddress[numSlaves][6] = {"00002", "00003", "00004"};

// ENCODER
volatile long temp, counter = 0;
long aux = 0;
long tracao = 25;

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
  //  // MEMORIA
  //  if (EEPROM[0] != 9)
  //  {
  //    EEPROM[0] = 9;
  //    EEPROM[1] = x0;
  //    EEPROM[2] = y0;
  //  }
  //  else {
  //    x0 = EEPROM[1];
  //    y0 = EEPROM[2];
  //  }

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
  Serial.print("Selecione a opcao\n");
  Serial.print("1 - PUXAR TODOS NA MESMA QUANTIDADE\n");
  Serial.print("2 - SOLTAR TODOS NA MESMA QUANTIDADE\n");
  //  Serial.print("3 - mover para frente\n");
  //  Serial.print("4 - mover para tras\n");
  //  Serial.print("5 - mover para esquerda\n");
  //  Serial.print("6 - mover para direita\n");
  Serial.print("11 - mover motor 1\n");
  Serial.print("22 - mover motor 2\n");
  Serial.print("33 - mover motor 3\n");
  Serial.print("44 - mover motor 4\n");
  Serial.print("35 - TESTE \n");


  while (Serial.available() == 0) {} //ESPERA
  int n = Serial.parseInt();
  Serial.print(n);
  Serial.print("\n");

  switch (n) {

    // PUXA TODOS NA MESMA QUANTIDADE
    case 1:
      Serial.print("--- PUXA TODOS NA MESMA QUANTIDADE ---\n\n");
      Serial.print("Digite o numero de passos (entre 100 e 3000)\n");
      while (Serial.available() == 0) {} //ESPERA
      aux = Serial.parseInt();
      Serial.print(aux);
      Serial.print("\n");
      if (aux < 0)
        aux = aux * (-1);
      // motor 4 puxando (POSITIVO)
      radio.openWritingPipe(slaveAddress[2]);
      radio.write(&aux, sizeof(aux));
      // motor 2 puxando (POSITIVO)
      radio.openWritingPipe(slaveAddress[0]);
      radio.write(&aux, sizeof(aux));
      // motor 3 puxando (POSITIVO)
      radio.openWritingPipe(slaveAddress[1]);
      radio.write(&aux, sizeof(aux));
      // motor 1 puxando (POSITIVO)
      TurnRight(aux);
      break;



    // SOLTA TODOS NA MESMA QUANTIDADE
    case 2:
      Serial.print("--- SOLTA TODOS NA MESMA QUANTIDADE ---\n\n");
      Serial.print("Digite o numero de passos (entre 100 e 5000)\n");
      while (Serial.available() == 0) {} //ESPERA
      aux = Serial.parseInt();
      Serial.print(aux);
      Serial.print("\n");
      if (aux > 0)
        aux = aux * (-1);
      // motor 4 soltando (NEGATIVO)
      radio.openWritingPipe(slaveAddress[2]);
      radio.write(&aux, sizeof(aux));
      // motor 3 soltando (NEGATIVO)
      radio.openWritingPipe(slaveAddress[1]);
      radio.write(&aux, sizeof(aux));
      // motor 2 soltando (NEGATIVO)
      radio.openWritingPipe(slaveAddress[0]);
      radio.write(&aux, sizeof(aux));
      // motor 1 soltando (NEGATIVO)
      TurnLeft(aux);
      break;




    // MOVER MOTORES INDIVIDUALMENTE
    // MOTOR 1 (MESTRE)
    case 11:
      Serial.print("Digite o numero de passos (5000 por exemplo)\n");
      Serial.print("+ PUXA\n");
      Serial.print("- SOLTA\n");
      while (Serial.available() == 0) {} //ESPERA
      aux = Serial.parseInt();
      Serial.print(aux);
      Serial.print("\n");
      if (aux < 0)
        TurnLeft(aux);

      else if (aux > 0)
        TurnRight(aux);

      else if (aux == 0)
        digitalWrite(ENABLE, LOW);
      break;
    // MOTOR 2
    case 22:
      Serial.print("Digite o numero de passos (5000 por exemplo)\n");
      Serial.print("+ PUXA\n");
      Serial.print("- SOLTA\n");
      while (Serial.available() == 0) {} //ESPERA
      aux = Serial.parseInt();
      Serial.print(aux);
      Serial.print("\n");
      radio.openWritingPipe(slaveAddress[0]);
      radio.write(&aux, sizeof(aux));
      break;
    // MOTOR 3
    case 33:
      Serial.print("Digite o numero de passos (5000 por exemplo)\n");
      Serial.print("+ PUXA\n");
      Serial.print("- SOLTA\n");
      while (Serial.available() == 0) {} //ESPERA
      aux = Serial.parseInt();
      Serial.print(aux);
      Serial.print("\n");
      radio.openWritingPipe(slaveAddress[1]);
      radio.write(&aux, sizeof(aux));
      break;
    // MOTOR 4
    case 44:
      Serial.print("Digite o numero de passos (5000 por exemplo)\n");
      Serial.print("+ PUXA\n");
      Serial.print("- SOLTA\n");
      while (Serial.available() == 0) {} //ESPERA
      aux = Serial.parseInt();
      Serial.print(aux);
      Serial.print("\n");
      radio.openWritingPipe(slaveAddress[2]);
      radio.write(&aux, sizeof(aux));
      break;



    // TESTE MOVIMENTO POR COORDENADAS
    case 35:
      Serial.print("--- TESTE ---\n\n");
      Serial.print("PONTO INICIAL: (");
      Serial.print(x0);
      Serial.print(",");
      Serial.print(y0);
      Serial.print(")\n");
      Serial.print("Digite a posicao em X desejada\n");
      while (Serial.available() == 0) {} //ESPERA
      xf = Serial.parseInt();
      Serial.print("Digite a posicao em Y desejada\n");
      while (Serial.available() == 0) {} //ESPERA
      yf = Serial.parseInt();
      Serial.print("PONTO FINAL:(");
      Serial.print(xf);
      Serial.print(",");
      Serial.print(yf);
      Serial.print(")\n");

      // Cálculo de quanto cada motor tem que mover
      distances[3] = cableDist(xd0, yd0, x0, y0, xf, yf) * (-1); // MOTOR 4 -> negativo pois convencionou-se - para soltar e + para puxar
      distances[2] = cableDist(xc0, yc0, x0, y0, xf, yf) * (-1); // MOTOR 3
      distances[1] = cableDist(xb0, yb0, x0, y0, xf, yf) * (-1); // MOTOR 2
      distances[0] = cableDist(xa0, ya0, x0, y0, xf, yf) * (-1); // MOTOR 1
      // Posição inicial vira a final agora
      x0 = xf;
      y0 = yf;

      Serial.print("MOVIMENTO MOTORES (EM PASSOS)\n");
      Serial.print("M1 = ");
      Serial.print(distances[0]);
      Serial.print("\n");
      Serial.print("M2 = ");
      Serial.print(distances[1]);
      Serial.print("\n");
      Serial.print("M3 = ");
      Serial.print(distances[2]);
      Serial.print("\n");
      Serial.print("M4 = ");
      Serial.print(distances[3]);
      Serial.print("\n");


      // salvando nova origem na memória
      //EEPROM[1] = x0;
      //EEPROM[2] = y0;



      // VERIFICA SE SOLTA PRIMEIRO
      if (distances[3] < 0)
      {
        // motor 4
        radio.openWritingPipe(slaveAddress[2]);
        radio.write(&distances[3], sizeof(distances[3]));
      }
      if (distances[2] < 0)
      {
        // motor 3
        radio.openWritingPipe(slaveAddress[1]);
        radio.write(&distances[2], sizeof(distances[2]));
      }
      if (distances[1] < 0)
      {
        // motor 2
        radio.openWritingPipe(slaveAddress[0]);
        radio.write(&distances[1], sizeof(distances[1]));
      }


      // VERIFICA SE PUXA
      if (distances[3] > 0)
      {
        // motor 4
        radio.openWritingPipe(slaveAddress[2]);
        radio.write(&distances[3], sizeof(distances[3]));
      }
      if (distances[2] > 0)
      {
        // motor 3
        radio.openWritingPipe(slaveAddress[1]);
        radio.write(&distances[2], sizeof(distances[2]));
      }
      if (distances[1] > 0)
      {
        // motor 2
        radio.openWritingPipe(slaveAddress[0]);
        radio.write(&distances[1], sizeof(distances[1]));
      }

      // MOTOR 1 SEMPRE É O ÚLTIMO POIS CASO O CONTRÁRIO O PROGRAMA ESPERA TERMINAR A
      // EXECUÇÃO DA FUNÇÃO (TurnLeft ou TurnRight) PARA MANDAR O CÓDIGO PARA OS RADIOS
      // motor 1
      if (distances[0] > 0)
        TurnRight(distances[0]);
      if (distances[0] < 0)
        TurnLeft(distances[0]);




      // TRAÇÃO PÓS MOVIMENTO
      //      Serial.print("TRACIONANDO TODOS ");
      //      // motor 3
      //      radio.openWritingPipe(slaveAddress[1]);
      //      radio.write(&tracao, sizeof(tracao));
      //      // motor 2
      //      radio.openWritingPipe(slaveAddress[0]);
      //      radio.write(&tracao, sizeof(tracao));
      //      // motor 4
      //      radio.openWritingPipe(slaveAddress[2]);
      //      radio.write(&tracao, sizeof(tracao));
      //      // motor 1
      //      TurnRight(tracao);
      //      break;
  }


}

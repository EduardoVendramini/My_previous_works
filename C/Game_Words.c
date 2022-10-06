#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<locale.h>
struct  Palavra {
char resposta[7];
char verifica[22];
};

void Funcprint(struct Palavra *palavra){
int i;
    for (i=0; i<26; ++i)
    {
        if(i<11){
            printf("%s\n",palavra[i].verifica);}
        if(i<21&&i>10){
            printf("%s\n",palavra[i].verifica);}
        if(i<24&&i>20){                                                //FUNCAO QUE PRINTA
            printf("%s\n",palavra[i].verifica);}
        if(i<26&&i>23){
            printf("%s\n",palavra[i].verifica);}}
return;
}

int main (){
setlocale(LC_ALL,"portuguese");
//var
int i,j,k,g=0,p;          //contadores
char usuario[8];
struct Palavra palavra[27];
strcpy(palavra[0].resposta,"ama");
strcpy(palavra[1].resposta,"ana");
strcpy(palavra[2].resposta,"asa");
strcpy(palavra[3].resposta,"ema");
strcpy(palavra[4].resposta,"mae");
strcpy(palavra[5].resposta,"mas");
strcpy(palavra[6].resposta,"ame");
strcpy(palavra[7].resposta,"mes");
strcpy(palavra[8].resposta,"nas");
strcpy(palavra[9].resposta,"nem");
strcpy(palavra[10].resposta,"sem");

strcpy(palavra[11].resposta,"amas");
strcpy(palavra[12].resposta,"anas");
strcpy(palavra[13].resposta,"asma");
strcpy(palavra[14].resposta,"asna");
strcpy(palavra[15].resposta,"emas");
strcpy(palavra[16].resposta,"maes");              //declaração de respostas
strcpy(palavra[17].resposta,"mana");
strcpy(palavra[18].resposta,"meas");
strcpy(palavra[19].resposta,"mesa");
strcpy(palavra[20].resposta,"sena");

strcpy(palavra[21].resposta,"amena");
strcpy(palavra[22].resposta,"manas");
strcpy(palavra[23].resposta,"mansa");

strcpy(palavra[24].resposta,"semana");
strcpy(palavra[25].resposta,"amenas");

//inicio

    for (i=0; i<26; ++i)
    {
        if(i<11)
        {
            strcpy(palavra[i].verifica,"[ ][ ][ ]");
        }
        if(i<21&&i>10)
        {
            strcpy(palavra[i].verifica,"[ ][ ][ ][ ]");
        }
        if(i<24&&i>20)
        {
            strcpy(palavra[i].verifica,"[ ][ ][ ][ ][ ]");          //declaração de strings como sendo [ ]
        }

        if(i<26&&i>23)
        {
            strcpy(palavra[i].verifica,"[ ][ ][ ][ ][ ][ ]");
        }
    }
Funcprint(palavra);                         //printando strings "cruas"
printf("Forme palavras com essas letras dadas:(obs: Utilize minúsculas, não use acentos e aperte 0 para finalizar. Não vale nome próprio)");
printf("\ns  m  e  a  a  n\n");
                    //printando palavra desordenada e instruções

for(j=0;j<40;j++){
fgets(usuario,9,stdin);                 //pedindo palavra ao usuário
g=strlen(usuario);
g-=1;
if(usuario[0]!='0')
    {
    if(g==3)
    {
        for(i=0; i<11; i++)
        {
            if(usuario[0]==palavra[i].resposta[0]&&usuario[1]==palavra[i].resposta[1]&&usuario[2]==palavra[i].resposta[2])
            {
                strcpy(palavra[i].verifica,usuario);
            }
        }
    }
     if(g==4){
        for(i=11; i<21; i++)
        {
            if(usuario[0]==palavra[i].resposta[0]&&usuario[1]==palavra[i].resposta[1]&&usuario[2]==palavra[i].resposta[2]&&usuario[3]==palavra[i].resposta[3])
            {
                strcpy(palavra[i].verifica,usuario);
            }
        }
    }
        if(g==5)
        {
            for(i=21; i<24; i++)
            {
                if(usuario[0]==palavra[i].resposta[0]&&usuario[1]==palavra[i].resposta[1]&&usuario[2]==palavra[i].resposta[2]&&usuario[3]==palavra[i].resposta[3]&&usuario[4]==palavra[i].resposta[4])
                {
                    strcpy(palavra[i].verifica,usuario);
                }
            }
        }
        if(g==6)
        {
            for(i=24; i<27; i++)
            {
                for(k=0,p=0;k<6;k++)
                {
                        if(usuario[k]==palavra[i].resposta[k])
                        {
                            p++;
                        }
                    }
                    if(p==6)
                    {
                        strcpy(palavra[i].verifica,usuario);
                    }
                }
            }
            system("cls");
    Funcprint(palavra);
printf("\ns  m  e  a  a  n\nAperte 0 para finalizar\n");
}
else{
    printf("\nfim de jogo");
}
}
//fim
return 0;
}

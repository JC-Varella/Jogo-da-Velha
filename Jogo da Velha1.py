from ast import While
import os
import random
from colorama import Fore, Back, Style

jogarNovamente="s"
jogadas=0
quemJoga=2 #1=CPU
maxJogadas=9
vit="n"
velha=[
       [" "," "," "],
       [" "," "," "],
       [" "," "," "]
       ]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | "  + velha[0][1] + " | " + velha[0][2])
    print("   ---------")
    print("1:  " + velha[1][0] + " | "  + velha[1][1] + " | " + velha[1][2])
    print("   ---------")
    print("2:  " + velha[2][0] + " | "  + velha[2][1] + " | " + velha[2][2])
    print("jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)
   
def jogadorJoga():
       global jogadas
       global quemJoga
       global maxJogadas
       if quemJoga==2 and jogadas<maxJogadas:
              try:
               l=int(input("Linha..: "))
               c=int(input("coluna..: "))
               while velha[1][c]!= " ":
                l=int(input("Linha..: "))
                c=int(input("Coluna..: "))
               velha[1][c]="X"
               quemJoga=1
               jogadas+=1
              except: 
               print:("jogadainvalida")
os.system("pause")
               #vit="n"
def cpuJoga():
         global jogadas
         global quemJoga
         global maxJogadas
if quemJoga==1 and jogadas<maxJogadas:
           l=random.randrange(0,3)
           c=random.randrange(0,3)
           while velha[1][c]!= " ":
              l=random.randrange(0,3)
              c=random.randrange(0,3)
              velha[1][c]="0"
              jogadas+=1
              quemJoga=2
              velha[1][c]="X"
              quemJoga+=1
              jogadas=2
               
#def verificarVitoria():
while True:
 tela()
jogadorJoga()
cpuJoga()
    
    

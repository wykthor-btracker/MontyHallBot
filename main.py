# -*- coding: utf-8 -*-
#!/usr/bin/env python

#imports#
from random import randint
#imports

#global Variables#
#global Variables

#classes#
class Apresentador():
    def __init__(self):
        self.portaCerta = randint(1,3)
        self.portas = [0,0,0]#0 para a porta que está fechada, 1 para a porta que está aberta

    def abrirPorta(self,escolhida):
        if self.portaCerta == escolhida:
            abrir = randint(1,3)
            while(abrir==self.portacerta):
                abrir = randint(1,3)
            self.portas[abrir] = 1
        else:
            portas = range(3)
            portas.pop(self.portaCerta)
            portas.pop(escolhida)
            self.portas[portas[0]] = 1

    def ganhou(self,escolhida):
        return(self.portaCerta == escolhida)

class Agente():
    def __init__(self):
        self.escolha = randint(1,3)
    def trocar(self):
        novaEscolha = randint(1,3)
        while novaEscolha==self.escolha:
            novaEscolha = randint(1,3)
        self.escolha = novaEscolha
#classes

#functions#
#functions

#main#
def main():
    return 0
#main

if __name__ == "__main__":
    main()

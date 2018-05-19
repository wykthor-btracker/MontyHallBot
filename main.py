# -*- coding: utf-8 -*-
#!/usr/bin/env python

#imports#
from random import randint,random
#imports

#global Variables#
#global Variables

#classes#
class Apresentador():
    def __init__(self):
        self.portaCerta = randint(0,2)
        self.portas = [0,0,0]#0 para a porta que está fechada, 1 para a porta que está aberta

    def reiniciar(self):
        self.portas = [0,0,0]
        self.portaCerta = randint(0,2)

    def abrirPorta(self,escolhida):
        if self.portaCerta == escolhida:
            abrir = randint(0,2)
            while(abrir==self.portaCerta):
                abrir = randint(0,2)
            self.portas[abrir] = 1
        else:
            portas = range(3)
            for i in portas:
                if(i != self.portaCerta and i != escolhida):
                    self.portas[i] = 1
    def ganhou(self,escolhida):
        return(self.portaCerta == escolhida)

class Agente():
    def __init__(self):
        self.escolha    = randint(0,2)
        self.trocar     = random()
        self.naoTrocar  = random()
        self.troquei = 0
        self.taxaDeAprendizagem = 0.01
        self.amortizacao = 0.9

    def randomizar(self):
        self.trocar = random()
        self.naoTrocar = random()

    def trocarPorta(self,portas):
        indicePortas = range(3)
        for i in indicePortas:
            if(i != self.escolha and portas[i]!= 1):
                novaEscolha = i
        self.escolha = novaEscolha

    def escolherAcao(self,portas):
        if(self.trocar > self.naoTrocar):
            self.trocarPorta(portas)
            self.troquei = 1
        #Se a esperança de ganho por trocar for maior que
        #não trocar, troque, se não, não faça nada.

    def atualizarValores(self,ganhou):
        if(ganhou):
            if(self.troquei):
                self.trocar+=self.trocar+self.taxaDeAprendizagem*(1+self.amortizacao*max(self.trocar,self.naoTrocar)-self.trocar)
            else:
                self.naoTrocar+=self.naoTrocar+self.taxaDeAprendizagem*(1+self.amortizacao*max(self.trocar,self.naoTrocar)-self.naoTrocar)
        else:
            if(self.troquei):
                self.trocar+=self.trocar+self.taxaDeAprendizagem*(-1+self.amortizacao*max(self.trocar,self.naoTrocar)-self.trocar)
            else:
                self.naoTrocar+=self.naoTrocar+self.taxaDeAprendizagem*(-1+self.amortizacao*max(self.trocar,self.naoTrocar)-self.naoTrocar)
        if(self.trocar>1):
            self.trocar = 1
        if(self.naoTrocar>1):
            self.naoTrocar = 1
#classes

#functions#
#functions

#main#
def main():
    apresentador = Apresentador()
    jogador = Agente()
    vitorias = 0
    derrotas = 0
    jogos = 0
    for i in range(100):
        jogador.randomizar()
        for i in range(10000):
            #jogador escolhe aleatoriamente que porta ele quer.
            apresentador.abrirPorta(jogador.escolha)
            #Apresentador abre uma porta e oferece a chance de
            #trocar de porta ao jogador
            jogador.escolherAcao(apresentador.portas)
            jogador.atualizarValores(apresentador.ganhou(jogador.escolha))
            if(apresentador.ganhou(jogador.escolha)):
                vitorias += 1
                #print("Ganhei!")
            else:
                derrotas += 1
                #print("Merda.")
            jogos+=1
            apresentador.reiniciar()
        print("Ganhei {0:.2f}% das vezes".format(100*(float(vitorias)/float(jogos))))
        print(jogador.trocar,jogador.naoTrocar)
    return 0
#main

if __name__ == "__main__":
    main()

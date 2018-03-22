'''
Conversor de layout para os arquivos de dados gerados para o SIAPC/PAD do TCE/RS

Este conversor de layout lê os dados constantes nos arquivos gerados no layout de
 importação pelo SIAPC/PAD e os trasnforma em outros formatos.

Este arquivo é o módulo principal que chama o módulo Controller.

Este software é distribuído sob a licença MIT.

'''
import sys
import os
import gui
import application

if __name__ == '__main__':
    GUI = gui.Window()
    CONVERSOR = application.App(GUI)
    CONVERSOR.run()

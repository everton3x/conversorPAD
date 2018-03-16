''' Módulo de controle do programa.
'''

import sys


class App:
    ''' Controlador do programa.
    '''

    def __init__(self, gui):
        ''' Construtor do controlador.
        '''

        self.gui = gui
        self.gui.app = self

    def run(self):
        ''' Executa o programa
        '''
        sys.exit(self.gui.show())

    def convert(self):
        ''' Inicia a conversão
        '''
        if self.gui.progress.get() < 100:
            self.gui.info.set('{}% processado...'.format(self.gui.progress.get()))
            self.gui.progress.set(self.gui.progress.get() + 1)
            self.gui.after(100, self.convert)
        else:
            self.gui.info.set('Conversão terminada!')

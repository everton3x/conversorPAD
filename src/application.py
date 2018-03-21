''' Módulo de controle do programa.
'''

import sys
import os
from datetime import datetime
from layout import *
from pandas import *


class App:
    ''' Controlador do programa.
    '''

    def __init__(self, gui):
        ''' Construtor do controlador.
        '''

        self.percentage = 0
        self.gui = gui
        self.gui.app = self
        self.reader = None
        self.writer = None

        self.date_parser = lambda d: datetime.strptime(d, '%d%m%Y').strftime('%d/%m/%Y')

    def run(self):
        ''' Executa o programa
        '''
        sys.exit(self.gui.show())

    def convert(self):
        ''' Inicia a conversão
        '''
        # Checagem básica
        if not os.path.exists(self.gui.source_dir.get()):
            self.gui.show_error('Diretório de origem {} não \
            encontrado!'.format(self.gui.source_dir.get()))

        if not os.path.exists(self.gui.output_dir.get()):
            self.gui.show_error('Diretório de destino {} não \
            encontrado!'.format(self.gui.output_dir.get()))

        if self.gui.output_name.get() == '':
            self.gui.show_error('Nome do arquivo de sáida {} \
            não é válido!'.format(self.gui.output_name.get()))

        self.sourceFiles = [os.path.join(self.gui.source_dir.get(), filename)
                            for filename in os.listdir(self.gui.source_dir.get())]
        layout = Layout()

        # Loop de read/parse/write arquivos
        increment = int(100 / len(self.sourceFiles))
        for source in self.sourceFiles:
            filename = os.path.basename(source)
            self.inprocess = os.path.splitext(filename)[0].lower()
            # print(self.inprocess)
            # data = self.sourceReader.read(filepath=source)
            if not layout.has_layout(self.inprocess):
                data = False
            else:
                data = read_fwf(source, colspecs=layout.colspecs(
                    self.inprocess), names=layout.names(self.inprocess), skiprows=1, skipfooter=1, dtype=layout.dtypes(self.inprocess), parse_dates=layout.date_cols(self.inprocess), date_parser=self.date_parser)
                # data = to_datetime(data, format='%d%m%Y')
                # data.apply(to_datetime, format='%d%m%Y')
                # data.apply(lambda d: d.strftime('d%/%m%Y'))
            # type(data)
            if data is not False:
                # print(csv_data)
                # salva os dados de acordo com o formato escolhido
                self._save_output(data)
            else:
                # print('{} não importado'.format(source))
                pass

            self.processing = os.path.basename(source)
            self.percentage += increment
            self.gui.after(100, self._update_progress)

        # if self.gui.progress.get() < 100:
        #     self.gui.info.set('{}% processado...'.format(self.gui.progress.get()))
        #     self.gui.progress.set(self.gui.progress.get() + 1)
        #     self.gui.after(100, self.convert)
        # else:
        #     self.gui.info.set('Conversão terminada!')
        return None

    def _update_progress(self):
        self.gui.progress.set(self.percentage)
        self.gui.info.set('Processando {} ({}%)'.format(
            self.processing, self.percentage))

    def _save_output(self, data):
        if self.gui.output_format.get() == 'CSV':
            self._save_to_csv(data)

    def _save_to_csv(self, data):
        output_path = os.path.join(
            self.gui.output_dir.get(), self.gui.output_name.get())
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        data.to_csv(os.path.join(output_path, self.inprocess + '.csv'),
                    sep=';', encoding=os.device_encoding(1), index=False)

        # print(csv)

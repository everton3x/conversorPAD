''' Módulo de controle do programa.
'''

import sys
import os
from datetime import datetime
from layout import *
# from pandas import *
import pandas as pd

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

        self.date_parser = lambda d: datetime.strptime(d, '%d%m%Y')

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
            return

        if not os.path.exists(self.gui.output_dir.get()):
            self.gui.show_error('Diretório de destino {} não \
            encontrado!'.format(self.gui.output_dir.get()))
            return

        if self.gui.output_name.get() == '':
            self.gui.show_error('Nome do arquivo de saída {} \
            não é válido!'.format(self.gui.output_name.get()))
            return

        if self.gui.output_format.get() == 'CSV':
            pass
        elif self.gui.output_format.get() == 'XLS':
            pass
        elif self.gui.output_format.get() == 'XLSX':
            pass
        else:
            self.gui.show_error('O formato de saída {} \
            não é válido!'.format(self.gui.output_format.get()))
            return

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
                data = pd.read_fwf(source, colspecs=layout.colspecs(
                    self.inprocess), names=layout.names(self.inprocess), skiprows=1, skipfooter=1, dtype=layout.dtypes(self.inprocess), parse_dates=layout.date_cols(self.inprocess), date_parser=self.date_parser, converters=layout.converters(self.inprocess), na_filter=False)
            if data is not False:
                self._save_output(data)
            else:
                pass

            self.processing = os.path.basename(source)
            self.percentage += increment
            # self.gui.after(100, self._update_progress)
            self._update_progress()
            # self.gui.update_idletasks()
            self.gui.update()

        if self.writer is not None:
            self.writer.save()
            self.writer = None

        self.gui.finish()

        return None

    def _update_progress(self):
        self.gui.progress.set(self.percentage)
        self.gui.info.set('Processando {} ({}%)'.format(
            self.processing, self.percentage))

    def _save_output(self, data):
        if self.gui.output_format.get() == 'CSV':
            self._save_to_csv(data)
        elif self.gui.output_format.get() == 'XLSX':
            self._save_to_xlsx(data)
        elif self.gui.output_format.get() == 'XLS':
            self._save_to_xls(data)

    def _save_to_csv(self, data):
        output_path = os.path.join(
            self.gui.output_dir.get(), self.gui.output_name.get())
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        data.to_csv(os.path.join(output_path, self.inprocess + '.csv'),
                    sep=';', encoding=os.device_encoding(1), index=False, date_format='%d/%m/%Y', float_format='%.2f', decimal=',')

    def _save_to_xlsx(self, data):
        output_path = os.path.join(
            self.gui.output_dir.get(), self.gui.output_name.get() + '.xlsx')
        # data.to_excel(output_path, index=False, float_format='%.2f', sheet_name=self.inprocess)
        self._save_to_excel(data, output_path)
        # self.get_excel_writer(output_path).save()

    def _save_to_xls(self, data):
        output_path = os.path.join(
            self.gui.output_dir.get(), self.gui.output_name.get() + '.xls')
        self._save_to_excel(data, output_path)
        # self.get_excel_writer(output_path).save()
        # data.to_excel(output_path, index=False, float_format='%.2f', sheet_name=self.inprocess)

    def _save_to_excel(self, data, filename):
        data.to_excel(self.get_excel_writer(filename), index=False, float_format='%.2f', sheet_name=self.inprocess)
        # self.get_excel_writer(filename).save()

    def get_excel_writer(self, filename):
        print(self.writer)
        if self.writer is None:
            # self.writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            self.writer = pd.ExcelWriter(filename)
        return self.writer

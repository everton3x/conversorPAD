''' Módulo de interface gráfica do usuário
'''

from tkinter import (Tk, LEFT, N, W, E, RIGHT, BOTTOM,
                     StringVar, DISABLED, Entry, Label, Frame,
                     Button, Radiobutton, DoubleVar, GROOVE,
                     CENTER, Message, X, HORIZONTAL, messagebox, NORMAL)
from tkinter import filedialog
from tkinter.ttk import Progressbar


class Window(Tk):
    ''' Janela principal do programa.
    '''
    # pylint: disable=too-many-instance-attributes

    def __init__(self):
        ''' Iniciador da classe
        '''
        super(Window, self).__init__()
        self.title('Conversor do PAD')
        # self.geometry('{width}x{height}'.format(width=800, height=400))

        # Texto introdutório
        text_intro = '''
Conversor do PAD é um conversor de layout que converte os dados gerados pelos sistemas informatizados com a finalidade de serem importados pelo SIAPC/PAD do TCE/RS.

Basicamente, o programa pega os dados e os converte para um formato diferente.
        '''
        self.intro = Message(self, text=text_intro,
                             justify=LEFT, anchor=N+W, padx=10, pady=10, width=700)
        self.intro.pack(fill=X)

        # Formulário com os campos de configuração
        form = Frame(self, padx=10, pady=10)
        form.pack()

        self._build_source_field(form)  # Seletor do diretório de origem
        self._build_output_field(form)  # Seletor do diretório de destino
        self._build_output_format(form)  # Seleção de formatos de saída
        self._build_output_name(form)  # Nome do arquivo de saída
        self._build_progress_bar(form)  # Barra de progresso
        self._build_start_button(form)  # Botão de conversão
        self._build_info_box(form)  # Caixa de informações
        self._build_status_bar()  # Barra de status

    def _build_source_field(self, form):
        ''' Seletor de diretório de origem
        '''
        self.source_field_label = Label(form, text='Diretório dos dados:', anchor=W)
        self.source_field_label.grid(row=0, column=0, sticky=W)

        self.source_dir = StringVar()
        self.source_dir.set('')
        # self.source_dir.set(r'M:\abase\ARQUIVOSPAD\2018\BIMESTRE1')

        self.source_field_input = Entry(form, state=DISABLED,
                                        textvariable=self.source_dir, width=100)
        self.source_field_input.grid(row=0, column=1)

        self.source_field_button = Button(form, text='Selecionar', command=self._choose_source_dir)
        self.source_field_button.grid(row=0, column=2)

    def _build_output_field(self, form):
        ''' Seletor de diretório de saída
        '''
        self.output_field_label = Label(form, text='Diretório de destino:', anchor=W)
        self.output_field_label.grid(row=1, column=0, sticky=W)

        self.output_dir = StringVar()
        self.output_dir.set('')
        # self.output_dir.set(r'C:\Users\Everton\Desktop')

        self.output_field_input = Entry(form, state=DISABLED,
                                        textvariable=self.output_dir, width=100)
        self.output_field_input.grid(row=1, column=1)

        self.output_field_button = Button(form, text='Selecionar', command=self._choose_output_dir)
        self.output_field_button.grid(row=1, column=2)

    def _build_output_format(self, form):
        ''' Seletor de formato de saída
        '''
        self.output_format_label = Label(form, text='Formatos de saída:', anchor=W)
        self.output_format_label.grid(row=2, column=0, sticky=W)

        formats_frame = Frame(form, relief=GROOVE, borderwidth=1)
        formats_frame.grid(row=2, column=1, sticky=W+E)

        self.output_format = StringVar()
        self.output_format.set('')

        for label in ('XLSX', 'XLS', 'CSV'):
            radio = Radiobutton(formats_frame, text=label,
                                value=label, variable=self.output_format, tristatevalue=0)
            radio.pack(anchor=W)
            radio.deselect()

    def _build_output_name(self, form):
        ''' Campo para nome da saída
        '''
        self.output_name_field_label = Label(form, text='Nome dos arquivos de saída:', anchor=W)
        self.output_name_field_label.grid(row=3, column=0, sticky=W)

        self.output_name = StringVar()
        self.output_name.set('')
        # self.output_name.set('teste_conversor_pad')

        self.output_name_field_input = Entry(form, textvariable=self.output_name, width=100)
        self.output_name_field_input.grid(row=3, column=1)

    def _build_progress_bar(self, form):
        ''' Barra de progresso
        '''
        self.progress_label = Label(form, text='Progresso', anchor=W)
        self.progress_label.grid(row=4, column=0, sticky=W)

        self.progress = DoubleVar()
        self.progress.set(0)

        self.progress_bar = Progressbar(form, maximum=100,
                                        orient=HORIZONTAL, variable=self.progress)
        self.progress_bar.grid(row=4, column=1, sticky=W+E)

    def _build_start_button(self, form):
        ''' Botão de início da conversão
        '''
        self.start_button = Button(form, text='Converter', command=self._start)
        self.start_button.grid(row=4, column=2)

    def _build_info_box(self, form):
        ''' Caixa de informações
        '''
        self.info = StringVar()
        self.info.set('Configure e inicie a conversão...')
        self.info_label = Label(form, textvariable=self.info, relief=GROOVE, anchor=W)
        self.info_label.grid(row=5, column=1, sticky=W+E)

    def _build_status_bar(self):
        ''' Barra de status
        '''
        self.status_bar = Frame(self, relief=GROOVE)
        self.status_bar.pack(side=BOTTOM, fill=X, expand=1)

        version_label = Label(self.status_bar, text='Versão 0.2', justify=LEFT, relief=GROOVE)
        version_label.pack(side=LEFT, fill=X)

        author_label = Label(self.status_bar,
                             text='Desenvolvido por Everton da Rosa <everton3x@gmail.com>',
                             justify=CENTER, relief=GROOVE)
        author_label.pack(side=LEFT, fill=X, expand=1)

        licence_label = Label(self.status_bar, text='Licenciado pela MIT Licence',
                              justify=RIGHT, relief=GROOVE)
        licence_label.pack(side=LEFT, fill=X)

    def show(self):
        ''' Mostra a janela do programa
        '''
        self.mainloop()
        return 0

    def _choose_source_dir(self):
        ''' Pede o diretório de origem
        '''
        options = {
            'parent': self,
            'title': 'Escolha o diretório onde estão os TXT do PAD'
        }

        selected = filedialog.askdirectory(**options)
        self.source_dir.set(selected)

    def _choose_output_dir(self):
        ''' Pede o diretório de destino
        '''
        options = {
            'parent': self,
            'title': 'Escolha o diretório onde serão salvas as conversões'
        }

        selected = filedialog.askdirectory(**options)
        self.output_dir.set(selected)

    def _start(self):
        ''' Inicia a conversão
        '''
        self.start_button.config(state=DISABLED)
        self.source_field_button.config(state=DISABLED)
        self.output_field_button.config(state=DISABLED)
        self.info.set('Processamento iniciado...')
        self.progress.set(0)
        self.app.convert()

    @staticmethod
    def show_error(text):
        ''' Exibe um pop up com uma mensagem de erro.
        '''

        messagebox.showerror('Um erro ocorreu!', text)
    
    @staticmethod
    def show_info(text):
        ''' Exibe um pop up com uma mensagem de informação.
        '''

        messagebox.showinfo('Atenção!', text)

    def finish(self):
        self.start_button.config(state=NORMAL)
        self.source_field_button.config(state=NORMAL)
        self.output_field_button.config(state=NORMAL)
        self.info.set('Processamento terminado!')
        self.progress.set(100)
        self.show_info('Processo terminado')

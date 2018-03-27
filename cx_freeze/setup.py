
import os
import sys
from  cx_Freeze import setup, Executable

''' Configura o diretório do setup.py como diretório de trabalho.

Permite chamar python setup.py build desde qualquer diretório'''
os.chdir(os.path.dirname(__file__))

''' Previne erro de TCL/TK não encontrado. '''
os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tk8.6'

base_directory = r'E:\python-virtualenv\conversorPAD'
src_directory = os.path.join(base_directory, 'src')
freeze_directory = os.path.join(base_directory, 'cx_freeze')
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Conversor do PAD',
    description='Um conversor de layout para os arquivos TXT do PAD',
    version='1.0',
    executables=[Executable(
        os.path.join(src_directory, 'conversor.py'),
        base=base,
        icon=os.path.join(freeze_directory, 'conversor.ico'),
        targetName='conversor.exe',
        shortcutName='Conversor do PAD')
    ],
    options = {
        "build_exe": {
            "packages": [
                'tkinter',
                'gui',
            ],
            'include_msvcr': True,
            'optimize': 2,
            'include_files': [
                os.path.join(freeze_directory, 'conversor.ico'),
                r'C:\Program Files (x86)\Python36-32\DLLs\tcl86t.dll',# Previne erros relacionados a falta do TCL
                r'C:\Program Files (x86)\Python36-32\DLLs\tk86t.dll',# Previne erros relacionados a falta do TK
                r'C:\Program Files (x86)\Python36-32\DLLs\sqlite3.dll',# Previne erros relacionados a falta do SQLite3
            ],
            'path': sys.path + [src_directory]
        }
    }
)

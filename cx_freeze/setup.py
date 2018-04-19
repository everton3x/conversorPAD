
import os
import sys
from  cx_Freeze import setup, Executable

''' Configura o diretório do setup.py como diretório de trabalho.

Permite chamar python setup.py build desde qualquer diretório'''
os.chdir(os.path.dirname(__file__))

if sys.platform == 'win32':
	''' Previne erro de TCL/TK não encontrado. '''
	os.environ['TCL_LIBRARY'] = r'C:\Users\Everton\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
	os.environ['TK_LIBRARY'] = r'C:\Users\Everton\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'
	base_directory = r'C:\Users\Everton\conversorPAD'
	
	exe_name = 'conversor.exe'
else:
	base_directory = r'/home/everton/conversorPAD/'
	exe_name = 'conversor.bin'
	base = None
	
src_directory = os.path.join(base_directory, 'src')
freeze_directory = os.path.join(base_directory, 'cx_freeze')

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Conversor do PAD',
    description='Um conversor de layout para os arquivos TXT do PAD',
    version='1.2',
    executables=[Executable(
        os.path.join(src_directory, 'conversor.py'),
        base=base,
        icon=os.path.join(freeze_directory, 'conversor.ico'),
        targetName=exe_name,
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
                os.path.join(freeze_directory, 'tcl86t.dll'),
                os.path.join(freeze_directory, 'tk86t.dll'),
                os.path.join(freeze_directory, 'sqlite3.dll'),
            ],
            'path': sys.path + [src_directory]
        }
    }
)

from Stack import Stack
from Scanner import scanner
from Parser import parser
from rich import print
import os
import sys

def main():
    file_name = input('Ingrese el nombre del archivo a escanear: ')
    if file_name == '': file_name = 'calculos.txt'
    if not os.path.exists(file_name):
        print('El archivo no existe.')
        sys.exit(1)
    
    try:
        with open(file_name, 'r') as file:
            lineas = file.read().splitlines()
    except IOError:
        print(f"El fichero '{file_name}' está bloqueado o no se puede leer.")

    for linea in lineas:
        if linea.strip() == '':
            continue
        print(linea)
        tokens = scanner(linea)
        if isinstance(tokens, tuple) and tokens[0] == 'Error':
            print(tokens[1])
            continue
        print(parser(tokens))
    
if __name__ == '__main__':
    main()
        
# J.O.S.E.S.
# Proyecto 6: Ensamblador de Nand2Tetris

Para llevar a cabo implementación del ensamblador para el Proyecto 6 del curso Nand2Tetris, se han desarrollado las siguientes clases:

1. **Symbol Table**
2. **Parser**
3. **Code**
4. **Assembler**


### 1. Symbol Table

La clase `SymbolTable` es responsable de gestionar las etiquetas y variables utilizadas en el código ensamblador. Permite agregar y buscar símbolos, asegurando que cada símbolo tenga un valor único.

```python
class SymbolTable:

    preSymbols =  {'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
    'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
    'SCREEN': 16384, 'KBD': 24576, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4}

    def __init__(self):
        """inicializa una nueva variable con los simbolos descritos en el diccionario preSymbols"""
        self.s_table = SymbolTable.preSymbols
    
    def contains(self, symbol):
        """determina si el simbolo pasado como argumento esta contenido en la tabla de simbolos"""
        return symbol in self.s_table

    def address(self, symbol):
        """retorna la dirección asociada con el simbolo que le pasamos como arguento a la función"""
        return self.s_table[symbol]

    def addPair(self, symbol, address):
        """añade el par de valores simbolo y dirección a la tabla"""
        self.s_table[symbol] = address
```

### 2. Parser

La clase `Parser` se encarga de analizar el código fuente, leyendo línea por línea. Esta clase convierte las instrucciones de ensamblador en un formato que puede ser procesado por la clase `Code`.

```python
import re
from typing import Literal

class Parser:
    def __init__(self, filepath) -> None:
        try:
            with open(filepath, 'r') as f:
                self.commands = list(filter(len, [re.sub(r'//.*$', '', l).strip() for l in f]))
        except FileNotFoundError:
            print(f"Could not find {filepath}")
    
    def hasMoreCommands(self) -> bool:
        return len(self.commands) > 0

    def next(self) -> None:
        self.command = self.commands.pop(0)

    def commandType(self) -> Literal['A', 'L', 'C']:
        if self.command[0] == '@':
            return A_COMMAND
        elif self.command[0] == '(' and self.command[-1] == ')':
            return L_COMMAND
        return C_COMMAND

    def symbol(self) -> str:
        return self.command.strip('@()')

    def dest(self) -> str:
        if '=' not in self.command:
            return ''
        return self.command.split('=')[0]

    def comp(self) -> str:
        return self.command.split('=')[-1].split(';')[0]

    def jump(self) -> str:
        if ';' not in self.command:
            return ''
        return self.command.split('=')[-1].split(';')[-1]

```

### 3. Code

La clase `Code` traduce las instrucciones de ensamblador a código máquina binario. Proporciona métodos para convertir instrucciones A y C a su representación binaria correspondiente.

```python
import sys
from Parser import *

class Code:
    dest_map = {'': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'}

    a0_comp = {'0': '101010', '1': '111111', '-1': '111010', 'D': '001100', 'A': '110000',
               '!D': '001101', '!A': '110001', '-D': '001111', '-A': '110011', 'D+1': '011111', 'A+1': '110111',
               'D-1': '001110', 'A-1': '110010', 'D+A': '000010', 'D-A': '010011', 'A-D': '000111', 'D&A': '000000',
               'D|A': '010101'}

    a1_comp = {'M': '110000', '!M': '110001', '-M': '110011', 'M+1': '110111', 'M-1': '110010', 'D+M': '000010',
               'D-M': '010011', 'M-D': '000111', 'D&M': '000000', 'D|M': '010101'}

    jump_map = {'': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}

    @staticmethod
    def dest(mnemonic):
        return Code.dest_map[mnemonic]

    @staticmethod
    def comp(mnemonic):
        if mnemonic in Code.a1_comp:
            return '1' + Code.a1_comp[mnemonic]
        elif mnemonic in Code.a0_comp:
            return '0' + Code.a0_comp[mnemonic]

    @staticmethod
    def jump(mnemonic):
        return Code.jump_map[mnemonic]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 Code.py FILE")
        sys.exit(1)

    for arg in sys.argv[1:]:
        p = Parser(arg)
        while p.hasMoreCommands():
            p.next()
            if (p.commandType() == A_COMMAND):
                instruction = "{0:016b}".format(int(p.symbol()))
            elif (p.commandType() == C_COMMAND):
                parts = []
                parts.append('111')
                parts.append(Code.comp(p.comp()))
                parts.append(Code.dest(p.dest()))
                parts.append(Code.jump(p.jump()))
                instruction = ''.join(parts)
            else:
                instruction = p.symbol()

            print(instruction)

```

### 4. Assembler

La clase `Assembler` integra las demás clases para realizar el ensamblaje completo del código. Procesa el archivo de entrada, utiliza `SymbolTable` para manejar etiquetas y variables, y finalmente produce un archivo de salida con el código máquina.

```python
import sys, os
from Parser import *
from Code import *
from SymbolTable import *

class Assembler:
    def __init__(self, files):
        self.files = files
        self.table = SymbolTable()

    def hasFile(self):
        return len(self.files) > 0
    
    def softPass(self):
        filename = self.files[0]
        p = Parser(filename)
        current_address = 0
        while p.hasMoreCommands():
            p.next()
            cmd_type = p.commandType()
            if cmd_type is A_COMMAND or cmd_type is C_COMMAND:
                current_address +=1
            elif cmd_type is L_COMMAND:
                self.table.addPair(p.symbol(), current_address)

    def getAddress(self, symbol):
        if symbol.isdigit():
            return symbol
        else:
            if not self.table.contains(symbol):
                self.table.addPair(symbol, self.current_address)
                self.current_address += 1
                return self.table.address(symbol)
            
    def translateFile(self):
        filename = self.files.pop(0)
        p = Parser(filename)
        if filename.endwith('.asm'):
            fileout = filename.replace('.asm', '.hack')
        else:
            fileout = filename + '.hack'
        f = open(fileout, 'w')
        print("Translating %s" % (filename))
        self.current_address = 16
        while p.hasMoreCommands():
            p.next()
            if p.commandType() is A_COMMAND:
                address = self.getAddress(p.symbol())
                instruction = '{0:016b}'.format(int(address))
            elif p.commandType is C_COMMAND:
                instruction = ''.join(['111', Code.comp(p.comp()), Code.dest(p.dest()), Code.jump(p.jump())])
            else:
                continue
            print(instruction, end='\n', file=f)
        f.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 Assembler.py FILE")
        sys.exit(1)
    a = Assembler(sys.argv[1:])
    while a.hasFile():
        a.softPass()
        a.translateFile()        
```


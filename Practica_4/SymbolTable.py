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
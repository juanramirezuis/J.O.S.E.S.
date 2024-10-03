# J.O.S.E.S.
# Proyecto 6: Ensamblador de Nand2Tetris

Este repositorio contiene la implementación del ensamblador para el Proyecto 6 del curso Nand2Tetris. En este proyecto, he desarrollado las siguientes clases:

1. **Symbol Table**
2. **Parser**
3. **Code**
4. **Assembler**

## Descripción de las Clases

### 1. Symbol Table

La clase `SymbolTable` es responsable de gestionar las etiquetas y variables utilizadas en el código ensamblador. Permite agregar y buscar símbolos, asegurando que cada símbolo tenga un valor único.

```python
# Ejemplo de uso de la clase SymbolTable
symbol_table = SymbolTable()
symbol_table.add_entry("LOOP", 10)
address = symbol_table.get_address("LOOP")
```

### 2. Parser

La clase `Parser` se encarga de analizar el código fuente, leyendo línea por línea. Esta clase convierte las instrucciones de ensamblador en un formato que puede ser procesado por la clase `Code`.

```python
# Ejemplo de uso de la clase Parser
parser = Parser("input.asm")
while parser.has_more_commands():
    parser.advance()
    command_type = parser.command_type()
```

### 3. Code

La clase `Code` traduce las instrucciones de ensamblador a código máquina binario. Proporciona métodos para convertir instrucciones A y C a su representación binaria correspondiente.

```python
# Ejemplo de uso de la clase Code
code = Code()
binary_instruction = code.translate("D=A")
```

### 4. Assembler

La clase `Assembler` integra las demás clases para realizar el ensamblaje completo del código. Procesa el archivo de entrada, utiliza `SymbolTable` para manejar etiquetas y variables, y finalmente produce un archivo de salida con el código máquina.

```python
# Ejemplo de uso de la clase Assembler
assembler = Assembler("input.asm", "output.hack")
assembler.assemble()
```

## Instrucciones para Ejecutar el Proyecto

1. Asegúrate de tener Python instalado en tu sistema.
2. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/nand2tetris-project6.git
   ```

3. Navega al directorio del proyecto:

   ```bash
   cd nand2tetris-project6
   ```

4. Ejecuta el ensamblador con un archivo de entrada:

   ```bash
   python assembler.py input.asm output.hack
   ```

## Contribuciones

Si deseas contribuir a este proyecto, no dudes en abrir un issue o enviar un pull request. Estoy abierto a sugerencias y mejoras.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.


------------------


### 1. **Mult.asm**
El archivo Mult.asm del proyecto 4 de Nand2tetris es un programa en ensamblador Hack que multiplica dos números almacenados en RAM[0] y RAM[1], guardando el resultado en RAM[2]. Utiliza un contador y un bucle para sumar repetidamente el valor de RAM[0] hasta alcanzar el valor en RAM[1], interpretando la multiplicación como una suma repetida.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/Assembler%20(2.5)%20-%20C__Users_SDNG_Documents_GitHub_J_O_S_E_S_Practica_3_Projecto4_Machine_Language_Programming_Mult.asm%209_22_2024%204_06_07%20PM.png)

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/CPU%20Emulator%20(2.5)%20-%20C__Users_SDNG_Documents_GitHub_J_O_S_E_S_Practica_3_Projecto4_Machine_Language_Programming_Mult.hack%209_22_2024%204_08_54%20PM.png)

### 2. **Fill.asm**
El archivo Fill.asm del proyecto 4 de Nand2Tetris es un programa en ensamblador que controla la pantalla gráfica (Screen). El programa verifica el valor del teclado (RAM[24576]), y dependiendo de si una tecla está presionada o no, llena la pantalla con un color o la limpia. Utiliza un bucle para escanear cada dirección de la memoria de la pantalla, escribiendo 0 o -1 en cada una, para limpiar o llenar la pantalla, respectivamente.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/Fill%20Emulator.png)

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/Fill%20Emulator%20Hack.png)
## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [[Ejemplo Texto azul](ejemplo_de_link.com)]


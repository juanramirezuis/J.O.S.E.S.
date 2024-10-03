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

```

### 2. Parser

La clase `Parser` se encarga de analizar el código fuente, leyendo línea por línea. Esta clase convierte las instrucciones de ensamblador en un formato que puede ser procesado por la clase `Code`.

```python

```

### 3. Code

La clase `Code` traduce las instrucciones de ensamblador a código máquina binario. Proporciona métodos para convertir instrucciones A y C a su representación binaria correspondiente.

```python
# lo ponen ahi
```

### 4. Assembler

La clase `Assembler` integra las demás clases para realizar el ensamblaje completo del código. Procesa el archivo de entrada, utiliza `SymbolTable` para manejar etiquetas y variables, y finalmente produce un archivo de salida con el código máquina.

```python
# lo ponen ahi
```

------------------


### 1. **Mult.asm**
El archivo Mult.asm del proyecto 4 de Nand2tetris es un programa en ensamblador Hack que multiplica dos números almacenados en RAM[0] y RAM[1], guardando el resultado en RAM[2]. Utiliza un contador y un bucle para sumar repetidamente el valor de RAM[0] hasta alcanzar el valor en RAM[1], interpretando la multiplicación como una suma repetida.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/Assembler%20(2.5)%20-%20C__Users_SDNG_Documents_GitHub_J_O_S_E_S_Practica_3_Projecto4_Machine_Language_Programming_Mult.asm%209_22_2024%204_06_07%20PM.png)

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/CPU%20Emulator%20(2.5)%20-%20C__Users_SDNG_Documents_GitHub_J_O_S_E_S_Practica_3_Projecto4_Machine_Language_Programming_Mult.hack%209_22_2024%204_08_54%20PM.png)

### 2. **Fill.asm**
El archivo Fill.asm del proyecto 4 de Nand2Tetris es un programa en ensamblador que controla la pantalla gráfica (Screen). El programa verifica el valor del teclado (RAM[24576]), y dependiendo de si una tecla está presionada o no, llena la pantalla con un color o la limpia. Utiliza un bucle para escanear cada dirección de la memoria de la pantalla, escribiendo 0 o -1 en cada una, para limpiar o llenar la pantalla, respectivamente.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/Fill%20Emulator.png)

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/Fill%20Emulator%20Hack.png)
### **Pruebas**
Una vez realizado nuestro propio ensamblador procedemos a probarlo para ello haremos uso de cuatro programas de prueba y el ensamblador suministrado por nand2Tetris entonces lo que debemos hacer es pasar las cuatro programas de prueba a nuestro ensamblador y el archivo punto yat que genera es decir la traducción a binario que genera debemos compararla con la traducción a binario que hace el ensamblador suministrado por nand2tetris.
- El primer programa ADD, este programa lo que hace es sumar los números 1, 2 y 3 y almacenarlos en rc.
  ![image](https://github.com/user-attachments/assets/9c04033f-a3ba-4376-97d7-b20a223eab94) ![image](https://github.com/user-attachments/assets/f7a3e63b-0f4b-441d-81e1-b670b02ac77d)


## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [[Ejemplo Texto azul](ejemplo_de_link.com)]


# J.O.S.E.S.
## Proyecto 4: Programacion en lenguaje de maquina.

### 1. **Mult.asm**
El archivo Mult.asm del proyecto 4 de Nand2tetris es un programa en ensamblador Hack que multiplica dos números almacenados en RAM[0] y RAM[1], guardando el resultado en RAM[2]. Utiliza un contador y un bucle para sumar repetidamente el valor de RAM[0] hasta alcanzar el valor en RAM[1], interpretando la multiplicación como una suma repetida.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/Assembler%20(2.5)%20-%20C__Users_SDNG_Documents_GitHub_J_O_S_E_S_Practica_3_Projecto4_Machine_Language_Programming_Mult.asm%209_22_2024%204_06_07%20PM.png)

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_3/Projecto4_Machine_Language_Programming/Imagenes/CPU%20Emulator%20(2.5)%20-%20C__Users_SDNG_Documents_GitHub_J_O_S_E_S_Practica_3_Projecto4_Machine_Language_Programming_Mult.hack%209_22_2024%204_08_54%20PM.png)

## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [[Ejemplo Texto azul](ejemplo_de_link.com)]
### 2. **Fill.asm**
El archivo Fill.asm del proyecto 4 de Nand2Tetris es un programa en ensamblador que controla la pantalla gráfica (Screen). El programa verifica el valor del teclado (RAM[24576]), y dependiendo de si una tecla está presionada o no, llena la pantalla con un color o la limpia. Utiliza un bucle para escanear cada dirección de la memoria de la pantalla, escribiendo 0 o -1 en cada una, para limpiar o llenar la pantalla, respectivamente.

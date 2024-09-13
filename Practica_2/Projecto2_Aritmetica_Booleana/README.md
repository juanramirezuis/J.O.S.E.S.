# J.O.S.E.S.
## Práctica 2: Logica Aritmetica.

En este taller se construyeron las compuertas logica, lo que nos dio como resultado un conjunto de chips basicos.

# Construyendo y entendiendo la Unidad Logica Aritmetica (ALU)

## Explicacion codigo para la creacion de los circuitos

### Half Adder Circuit

Un circuito digital Half Adder es un tipo de circuito lógico que se utiliza en la aritmética digital para realizar la suma binaria de dos bits. 
Este tipo de circuito toma dos entradas binarias, A y B, y produce dos salidas, una llamada “suma” (S) y otra llamada “acarreo” (Carry).

![image](https://github.com/user-attachments/assets/3b10d451-85e3-4cbf-9782-daf391a662db)

La operación de suma binaria de dos entradas realizada por un Half Adder se realiza de la siguiente manera:

(0+0=0 | 0) Si A y B son ambos 0, la suma S es 0 y el acarreo C es 0.

(1+0=1 | 0) Si A es 1 y B es 0, la suma S es 1 y el acarreo C es 0.

(0+1=1 | 0) Si A es 0 y B es 1, la suma S es 1 y el acarreo C es 0.

(1+1=0 | 1) Si A y B son ambos 1, la suma S es 0 y el acarreo C es 1.

- **Representación del Half Adder en la tabla de la verdad**


![image](https://github.com/user-attachments/assets/37dfc838-6761-4e67-a5f2-5eccfcdfa5b5)


- **Su esquema e implementación**

![image](https://github.com/user-attachments/assets/b690a5cd-ee31-4971-82f5-5e0ffe497589)


### Full Adder Circuit

Al igual que el Half Adder el Full Adder también es un tipo de circuito lógico que se utiliza en la aritmética digital para realizar la suma binaria de tres bits. 
Este tipo de circuito toma tres entradas binarias, A, B y un acarreo de entrada (Cin), y produce dos salidas, una llamada “suma” (S) y otra llamada “acarreo” (Carry).

La operación de suma binaria realizada por un Full Adder se realiza de la siguiente manera:

Se suma A y B y se agrega el acarreo de entrada Cin. Si el resultado es 0, la suma S es 0 y el acarreo Carry es 0.

Si el resultado de la suma de A, B y Cin es 1, la suma S es 1 y el acarreo Carry es 0.

Si el resultado de la suma de A, B y Cin es 2, la suma S es 0 y el acarreo Carry es 1.

Si el resultado de la suma de A, B y Cin es 3, la suma S es 1 y el acarreo Carry es 1.

- **Representación del Full Adder en la tabla de la verdad**


![image](https://github.com/user-attachments/assets/4b58a09b-97af-4c90-b7f3-d08bfc253c76)


- **Su esquema e implementación**

![image](https://github.com/user-attachments/assets/7394a3a8-7a8c-479b-b44c-fa2ea7c229dd)


El chip FullAdder realiza la suma de tres bits: dos bits de entrada (a y b) y un bit de acarreo de entrada (c). Utiliza dos sumadores parciales (HalfAdder) para calcular la suma y los acarreos intermedios, y luego combina los acarreos generados con una puerta lógica OR para obtener el acarreo final. Este diseño permite al FullAdder manejar la suma binaria con acarreo, una función esencial en la aritmética digital.

### 16-Bit Adder

El chip Add16 es un sumador de 16 bits que realiza la suma de dos números binarios de 16 bits en complemento a dos. 
Este chip utiliza una cadena de 16 sumadores completos, cada uno de los cuales maneja una posición de bit específica en los números de entrada. Cada sumador completo toma dos bits de las entradas `a` y `b`, junto con un bit de acarreo de entrada, y produce un bit de suma y un bit de acarreo de salida. 

![image](https://github.com/user-attachments/assets/4a413ed3-4e09-4aaf-ba95-f6f082ad0059)

El acarreo de salida de un sumador completo se pasa como acarreo de entrada al siguiente sumador en la cadena. Este proceso se repite para cada bit, desde el menos significativo hasta el más significativo. Al final, los bits de suma de cada sumador forman el resultado final de la suma de los dos números de 16 bits. Es importante destacar que, aunque el último sumador completo genera un bit de acarreo final, este acarreo más significativo se ignora en el diseño del chip, por lo que el resultado es un vector de 16 bits que refleja la suma de las dos entradas.

- **Implementacion del 16Bit Adder**

![image](https://github.com/user-attachments/assets/65d28cb3-b28c-478d-b8d8-be74faf40229)


### 16-Bit Incrementer

El chip Inc16 se utiliza para incrementar un número binario de 16 bits en 1. Para lograr esto, el Inc16 emplea el chip Add16, un sumador de 16 bits. En su funcionamiento, la entrada in del Inc16 se conecta directamente al primer operando del Add16, mientras que el segundo operando b se configura para representar el valor binario de 1, con b[0] establecido en true (o 1) y los demás bits en false (o 0). Al sumar el número de entrada in con este valor binario de 1, el Add16 produce la suma, la cual es emitida en la salida out. De esta manera, Inc16 incrementa el valor de entrada en 1 y proporciona el resultado actualizado en su salida.

## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [[From NAND To Tetris - Logic Gates Lab](https://www.youtube.com/watch?v=Mzy0RG9Z1Ak&t=78s)](https://youtu.be/Wl53tFc5WYQ?si=89A2tz64oT-TPEhA)
 - https://medium.com/@massin.laaouaj/half-adder-vs-full-adder-estructura-de-computadores-d3bbee8dbd5c#:~:text=Un%20circuito%20digital%20Half%20Adder,%E2%80%9Cacarreo%E2%80%9D%20(Cout).
   
**Imagenes:**

 - [https://circuitdigest.com/sites/default/files/inlineimages/u/4-to-1-MUX-using-three-2-to-1-MUX.png](https://edurev.in/question/3246991/A-16-bit-ripple-carry-adder-is-realized-using-16-identical-full-adders--FA--as-shown-in-the-figure--)
 - [https://www.electronicshub.org/wp-content/uploads/2021/04/Block-Diagram-of-16-to-1-Multiplexer.jpg](https://evaysusapuntes.blogspot.com/2016/06/sumador-y-restador-con-puertas-logicas.html)

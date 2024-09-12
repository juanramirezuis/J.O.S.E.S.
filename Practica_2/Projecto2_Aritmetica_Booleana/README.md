# J.O.S.E.S.
## Práctica 2: Logica Aritmetica.

En este taller se construyeron las compuertas logica, lo que nos dio como resultado un conjunto de chips basicos.

### Objetivo
aca se pone el objetivo



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

Representación del Half Adder en la tabla de la verdad:


![image](https://github.com/user-attachments/assets/37dfc838-6761-4e67-a5f2-5eccfcdfa5b5)


Su esquema e implementación:

![image](https://github.com/user-attachments/assets/b690a5cd-ee31-4971-82f5-5e0ffe497589)


### Full Adder Circuit

Al igual que el Half Adder el Full Adder también es un tipo de circuito lógico que se utiliza en la aritmética digital para realizar la suma binaria de tres bits. 
Este tipo de circuito toma tres entradas binarias, A, B y un acarreo de entrada (Cin), y produce dos salidas, una llamada “suma” (S) y otra llamada “acarreo” (Carry).

La operación de suma binaria realizada por un Full Adder se realiza de la siguiente manera:

Se suma A y B y se agrega el acarreo de entrada Cin. Si el resultado es 0, la suma S es 0 y el acarreo Carry es 0.
Si el resultado de la suma de A, B y Cin es 1, la suma S es 1 y el acarreo Carry es 0.
Si el resultado de la suma de A, B y Cin es 2, la suma S es 0 y el acarreo Carry es 1.
Si el resultado de la suma de A, B y Cin es 3, la suma S es 1 y el acarreo Carry es 1.

Representación del Half Adder en la tabla de la verdad:


![image](https://github.com/user-attachments/assets/4b58a09b-97af-4c90-b7f3-d08bfc253c76)


Su esquema e implementación:

![image](https://github.com/user-attachments/assets/79707b3f-12de-4110-9674-2113de2a258e)


En este circuito, se combinan dos circuitos sumadores simples (half adder) utilizando una compuerta OR. El primer sumador simple tiene dos entradas binarias de un solo bit, A y B. Como sabemos, el sumador simple genera dos salidas: Suma y Acarreo. La salida 'Suma' del primer sumador será la primera entrada del segundo sumador simple, y la salida 'Acarreo' del primer sumador será la segunda entrada del segundo sumador simple. El segundo sumador simple generará nuevamente 'Suma' y 'Acarreo'. El resultado final del circuito sumador completo (full adder) será el bit de 'Suma'. Para obtener la salida final del 'Acarreo', conectamos las salidas de 'Acarreo' del primer y del segundo sumador a una compuerta OR. El resultado de la compuerta OR será el acarreo final del circuito sumador completo.

El MSB (bit más significativo) está representado por el bit final de 'Acarreo'


### 16-Bit Adder

Un sumador de 16 bits basado en sumadores completos se encarga de sumar dos números binarios de 16 bits, procesándolos bit a bit. Cada número binario se compone de 16 dígitos, y el sumador utiliza un sumador completo (full adder) para cada par de bits. El proceso comienza en el bit menos significativo (bit 0) de ambos números, donde el sumador completo toma los bits de entrada A y B, más un posible acarreo inicial (generalmente 0), y calcula dos salidas: un bit de Suma y un Acarreo.

El bit de Suma es parte del resultado final en esa posición, mientras que el bit de Acarreo se transfiere al siguiente sumador completo, que sumará el siguiente par de bits (en la posición 1) junto con el acarreo recibido. Este proceso se repite hasta que los 16 bits han sido sumados. En la posición final (bit 15), el sumador completo produce un bit de suma para el bit más significativo y un acarreo final que puede ser utilizado para futuras operaciones si es necesario. El sumador de 16 bits divide la suma en una cadena de sumadores completos, donde cada uno gestiona la suma de un bit y transfiere el acarreo a la siguiente posición, garantizando una suma correcta de los 16 bits.

- **Implementacion del 16Bit Adder**

![image](https://github.com/user-attachments/assets/e04d8e95-a5a9-4239-a602-5c4e2e781300)

### 16-Bit Incrementer

Este circuito lo que hara es que la entrada que se ingrese, la cual sera un numero de 16 bits, se le suma 1 (un bit) por lo que su implementacion es bastante sencilla ya que se usa un 
sumador completo de 16 bits, en donde su primera entrada sera la misma entrada del incrementador, y la segunda entrada sera el numero 1 en formato de 16 bits

## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [From NAND To Tetris - Logic Gates Lab](https://www.youtube.com/watch?v=Mzy0RG9Z1Ak&t=78s)
 - https://medium.com/@massin.laaouaj/half-adder-vs-full-adder-estructura-de-computadores-d3bbee8dbd5c#:~:text=Un%20circuito%20digital%20Half%20Adder,%E2%80%9Cacarreo%E2%80%9D%20(Cout).
Imagenes:
 - https://circuitdigest.com/sites/default/files/inlineimages/u/4-to-1-MUX-using-three-2-to-1-MUX.png
 - https://www.electronicshub.org/wp-content/uploads/2021/04/Block-Diagram-of-16-to-1-Multiplexer.jpg
 - https://d2vlcm61l7u1fs.cloudfront.net/media%2F268%2F26880fba-979c-4637-b9c2-d2da3aae7580%2FphpHS1AKM.png

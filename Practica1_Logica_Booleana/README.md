# J.O.S.E.S.
## Práctica 1: Logica Booleana.

En este taller se construyeron las compuertas logica, lo que nos dio como resultado un conjunto de chips basicos.

### Preguntas

1. ¿Que consideraciones importantes debe tener en cuenta para trabajar con Nand2Tetris?:
   
   Para trabajar con Nand2Tetris, es fundamental tener una comprensión básica de conceptos de computación, como puertas lógicas y arquitectura de computadoras, y seguir el curso en orden, ya que cada capítulo se
   basa en el anterior. El entorno de desarrollo adecuado, como Java para ejecutar los simuladores, y la paciencia para construir cada componente desde cero son claves. Es crucial probar y verificar cada paso 
   utilizando las herramientas de simulación proporcionadas, y participar en la comunidad para resolver dudas y compartir avances.
   
3. ¿Qué otras herramientas similares a Nand2Tetris existen?:

   Dos herramientas similares a Nand2Tetris son **Logisim** y **Digital**. Logisim es una herramienta visual e intuitiva para diseñar y simular circuitos lógicos digitales, ideal para aprender sobre puertas lógicas    y arquitectura básica de computadoras. Digital también permite diseñar, simular y probar circuitos digitales, ofreciendo un entorno flexible para crear circuitos combinacionales, secuenciales y microprocesadores    simples. Ambas son excelentes para complementar el aprendizaje en diseño de circuitos y arquitectura de sistemas.

### 1. **NOT**
La puerta lógica NOT invierte el valor de entrada. Si la entrada es 1, la salida es 0, y viceversa.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/Not.JPG?raw=true)

| Entrada (A) | Salida (¬A) |
|:-----------:|:-----------:|
|      0      |      1      |
|      1      |      0      |

### 2. **AND**
La puerta lógica **AND** da una salida de 1 solo si ambas entradas son 1. En cualquier otro caso, la salida es 0.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/AND.png?raw=true)

| Entrada (A) | Entrada (B) | Salida (A AND B) |
|:-----------:|:-----------:|:----------------:|
|      0      |      0      |        0         |
|      0      |      1      |        0         |
|      1      |      0      |        0         |
|      1      |      1      |        1         |

### 3. **OR**
La puerta lógica **OR** da una salida de 1 si al menos una de las entradas es 1. Solo da 0 cuando ambas entradas son 0.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/OR.png?raw=true)

| Entrada (A) | Entrada (B) | Salida (A OR B) |
|:-----------:|:-----------:|:---------------:|
|      0      |      0      |       0         |
|      0      |      1      |       1         |
|      1      |      0      |       1         |
|      1      |      1      |       1         |

### 4. **XOR**
La puerta lógica **XOR** da una salida de 1 solo si las entradas son diferentes. Si ambas entradas son iguales, la salida es 0.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/XOR.png?raw=true)

| Entrada (A) | Entrada (B) | Salida (A XOR B) |
|:-----------:|:-----------:|:----------------:|
|      0      |      0      |        0         |
|      0      |      1      |        1         |
|      1      |      0      |        1         |
|      1      |      1      |        0         |

### 5. **MUX**
Un **MUX** selecciona una de varias entradas de datos en función de las señales de selección y la envía como salida.

Para un MUX de 2 a 1 (una señal de selección S):

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/MUX.png?raw=true)

| Entrada (A) | Entrada (B) | Selección (S) | Salida (Y) |
|:-----------:|:-----------:|:-------------:|:----------:|
|      0      |      0      |       0       |     0      |
|      0      |      1      |       0       |     0      |
|      1      |      0      |       1       |     0      |
|      1      |      1      |       1       |     1      |

### 6. **DMUX**
Un **DMUX** dirige una entrada a una de varias salidas, en función de las señales de selección.

Para un DMUX de 1 a 2 (una señal de selección S):

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/DMUX.png?raw=true)

| Entrada (A) | Selección (S) | Salida (Y0) | Salida (Y1) |
|:-----------:|:-------------:|:-----------:|:-----------:|
|      0      |       0       |      0      |      0      |
|      1      |       0       |      1      |      0      |
|      0      |       1       |      0      |      0      |
|      1      |       1       |      0      |      1      |

### 7. **16-bit NOT**
Una **16-bit NOT** es una operación que aplica la puerta lógica **NOT** a cada uno de los 16 bits de un número de 16 bits, invirtiendo cada bit individualmente.
Para cada bit individual en una operación de 16-bit NOT, la tabla de verdad es la misma que la de la puerta NOT:

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/16bit%20NOT.png?raw=true)

| Entrada (Bit) | Salida (¬Bit) |
|:-------------:|:-------------:|
|       0       |       1       |
|       1       |       0       |

### 8. **16-bit AND**
Una **16-bit AND** es una operación que aplica la puerta lógica **AND** a cada uno de los 16 bits de dos números de 16 bits, combinando cada par de bits correspondientes de las dos entradas.
Para cada par de bits individuales en una operación de 16-bit AND, la tabla de verdad es la misma que la de la puerta AND:

![alt text]([https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/16bit%20NOT.png?raw=true](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/16-bit%20And.PNG?raw=true))

| Entrada A (Bit) | Entrada B (Bit) | Salida (A ∧ B) |
|:---------------:|:---------------:|:---------------:
|        0        |        0        |        0       |
|        0        |        1        |        0       |
|        1        |        0        |        0       |
|        1        |        1        |        1       |

## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [From NAND To Tetris - Logic Gates Lab](https://www.youtube.com/watch?v=Mzy0RG9Z1Ak&t=78s)

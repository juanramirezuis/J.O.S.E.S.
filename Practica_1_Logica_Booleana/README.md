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

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/16-bit%20And.PNG?raw=true)

| Entrada A (Bit) | Entrada B (Bit) | Salida (A ∧ B) |
|:---------------:|:---------------:|:---------------:
|        0        |        0        |        0       |
|        0        |        1        |        0       |
|        1        |        0        |        0       |
|        1        |        1        |        1       |

### 9. **8-Way OR**
Un **8-Way OR** es una operación que toma ocho entradas y las combina utilizando la puerta lógica OR. La salida será 1 si al menos una de las ocho entradas es 1:

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/8-Way%20Or.PNG?raw=true)

| Entrada 0 | Entrada 1 | Entrada 2 | Entrada 3 | Entrada 4 | Entrada 5 | Entrada 6 | Entrada 7 | Salida |
|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:------:|
|     0     |     0     |     0     |     0     |     0     |     0     |     0     |     0     |    0   |
|     0     |     0     |     0     |     0     |     0     |     0     |     0     |     1     |    1   |
|     0     |     0     |     0     |     0     |     0     |     0     |     1     |     0     |    1   |
|     0     |     0     |     0     |     0     |     0     |     1     |     0     |     0     |    1   |
|     0     |     0     |     0     |     0     |     1     |     0     |     0     |     0     |    1   |
|     0     |     0     |     0     |     1     |     0     |     0     |     0     |     0     |    1   |
|     0     |     0     |     1     |     0     |     0     |     0     |     0     |     0     |    1   |
|     0     |     1     |     0     |     0     |     0     |     0     |     0     |     0     |    1   |
|     1     |     0     |     0     |     0     |     0     |     0     |     0     |     0     |    1   |
|     1     |     1     |     0     |     0     |     0     |     0     |     0     |     0     |    1   |
|     1     |     0     |     1     |     0     |     0     |     0     |     0     |     0     |    1   |
|     1     |     0     |     0     |     1     |     0     |     0     |     0     |     0     |    1   |
|     1     |     0     |     0     |     0     |     1     |     0     |     0     |     0     |    1   |
|     1     |     0     |     0     |     0     |     0     |     1     |     0     |     0     |    1   |
|     1     |     0     |     0     |     0     |     0     |     0     |     1     |     0     |    1   |
|     1     |     0     |     0     |     0     |     0     |     0     |     0     |     1     |    1   |
|     1     |     1     |     1     |     1     |     1     |     1     |     1     |     1     |    1   |



### 10. **4-Way DEMUX**
Un **4-Way DEMUX**  un dispositivo digital que toma una única entrada y la dirige a una de cuatro posibles salidas, basándose en el valor de las líneas de selección.
Se utilizan 2 líneas de selección para elegir a cuál de las 4 salidas se dirige la entrada:

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/4-Way%20Demux.PNG?raw=true)

| Selección S1| Selección S0 | Salida 0 | Salida 1 | Salida 2 | Salida 2 |
|:-----------:|:------------:|:--------:|:--------:|:--------:|:--------:|
|      0      |       0      |     1    |    0     |     0    |    0     |
|      0      |       1      |     0    |    1     |     0    |    0     |
|      1      |       0      |     0    |    0     |     1    |    0     |
|      1      |       1      |     0    |    0     |     0    |    1     |

### 11. **8-Way DEMUX**
Un **8-Way DEMUX** es un dispositivo digital que toma una única entrada y la distribuye a una de ocho posibles salidas, basada en el valor de las líneas de selección.
se utiliza una configuración de 3 líneas de selección para elegir a cuál de las 8 salidas se dirige la entrada:

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/4-Way%20Demux.PNG?raw=true)

| Selección S2 | Selección S1 | Selección S0 | Salida 0 | Salida 1 | Salida 2 | Salida 3 | Salida 4 | Salida 5 | Salida 6 | Salida 7 |
|:------------:|:------------:|:------------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|      0       |       0      |       0      |     1    |     0    |     0    |     0    |     0    |     0    |     0    |     0    |
|      0       |       0      |       1      |     0    |     1    |     0    |     0    |     0    |     0    |     0    |     0    |
|      0       |       1      |       0      |     0    |     0    |     1    |     0    |     0    |     0    |     0    |     0    |
|      0       |       1      |       1      |     0    |     0    |     0    |     1    |     0    |     0    |     0    |     0    |
|      1       |       0      |       0      |     0    |     0    |     0    |     0    |     1    |     0    |     0    |     0    |
|      1       |       0      |       1      |     0    |     0    |     0    |     0    |     0    |     1    |     0    |     0    |
|      1       |       1      |       0      |     0    |     0    |     0    |     0    |     0    |     0    |     1    |     0    |
|      1       |       1      |       1      |     0    |     0    |     0    |     0    |     0    |     0    |     0    |     1    |

### 12. **16-bit MUX**
Un **16-bit MUX**  es un dispositivo que selecciona una de las 16 entradas de 16 bits y la dirige a una salida de 16 bits, basándose en un conjunto de líneas de selección:

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/16-bit%20MUXs.png?raw=true)

| Selección \(S_3\) | Selección \(S_2\) | Selección \(S_1\) | Selección \(S_0\) | Salida |
|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:------:|
|         0         |         0         |         0         |         0         |   D0   |
|         0         |         0         |         0         |         1         |   D1   |
|         0         |         0         |         1         |         0         |   D2   |
|         0         |         0         |         1         |         1         |   D3   |
|         0         |         1         |         0         |         0         |   D4   |
|         0         |         1         |         0         |         1         |   D5   |
|         0         |         1         |         1         |         0         |   D6   |
|         0         |         1         |         1         |         1         |   D7   |
|         1         |         0         |         0         |         0         |   D8   |
|         1         |         0         |         0         |         1         |   D9   |
|         1         |         0         |         1         |         0         |   D10  |
|         1         |         0         |         1         |         1         |   D11  |
|         1         |         1         |         0         |         0         |   D12  |
|         1         |         1         |         0         |         1         |   D13  |
|         1         |         1         |         1         |         0         |   D14  |
|         1         |         1         |         1         |         1         |   D15  |


### 13. **4-Way 16-bit MUX**
Un **4-Way 16-bit MUX**  tiene 4 entradas, cada una de 16 bits, y utiliza 2 líneas de selección para elegir cuál de las 4 entradas se dirige a la salida. La salida también es de 16 bits.


![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/4way16bit.png?raw=true)

| Selección \(S_1\) | Selección \(S_0\) | Salida (16 bits) |
|:-----------------:|:-----------------:|:----------------:|
|         0         |         0         |    Entrada 0     |
|         0         |         1         |    Entrada 1     |
|         1         |         0         |    Entrada 2     |
|         1         |         1         |    Entrada 3     |

### 14. **8-Way 16-bit MUX**
Un **8-Way 16-bit MUX**  es un dispositivo que selecciona una de varias entradas de 16 bits y la envía a la salida, basada en las señales de selección. En este caso, el MUX tiene 8 entradas de 16 bits y 3 líneas de selección para elegir cuál de las 8 entradas se dirigirá a la salida:


![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/16-bit%20MUX2.png?raw=true)

| \(S_2\) | \(S_1\) | \(S_0\) | Entrada 0 | Entrada 1 | Entrada 2 | Entrada 3 | Entrada 4 | Entrada 5 | Entrada 6 | Entrada 7 | Salida (Seleccionada) |
|:-------:|:-------:|:-------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:----------------------:|
|    0    |    0    |    0    |     D_0   |     -     |     -     |     -     |     -     |     -     |     -     |     -     |           D_0          |
|    0    |    0    |    1    |     -     |     D_1   |     -     |     -     |     -     |     -     |     -     |     -     |           D_1          |
|    0    |    1    |    0    |     -     |     -     |     D_2   |     -     |     -     |     -     |     -     |     -     |           D_2          |
|    0    |    1    |    1    |     -     |     -     |     -     |     D_3   |     -     |     -     |     -     |     -     |           D_3          |
|    1    |    0    |    0    |     -     |     -     |     -     |     -     |     D_4   |     -     |     -     |     -     |           D_4          |
|    1    |    0    |    1    |     -     |     -     |     -     |     -     |     -     |     D_5   |     -     |     -     |           D_5          |
|    1    |    1    |    0    |     -     |     -     |     -     |     -     |     -     |     -     |     D_6   |     -     |           D_6          |
|    1    |    1    |    1    |     -     |     -     |     -     |     -     |     -     |     -     |     -     |     D_7   |           D_7          |

## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [From NAND To Tetris - Logic Gates Lab](https://www.youtube.com/watch?v=Mzy0RG9Z1Ak&t=78s)
Imagenes:
 - https://circuitdigest.com/sites/default/files/inlineimages/u/4-to-1-MUX-using-three-2-to-1-MUX.png
 - https://www.electronicshub.org/wp-content/uploads/2021/04/Block-Diagram-of-16-to-1-Multiplexer.jpg
 - https://d2vlcm61l7u1fs.cloudfront.net/media%2F268%2F26880fba-979c-4637-b9c2-d2da3aae7580%2FphpHS1AKM.png

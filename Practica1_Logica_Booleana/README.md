# J.O.S.E.S.
## Práctica 1: Logica Booleana.

En este taller se construyeron las compuertas logica, lo que nos dio como resultado un conjunto de chips basicos.

### 1. **NOT (Negación)**
La puerta lógica **NOT** invierte el valor de entrada. Si la entrada es `1`, la salida es `0`, y viceversa.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/Not.JPG?raw=true)

| Entrada (A) | Salida (¬A) |
|:-----------:|:-----------:|
|      0      |      1      |
|      1      |      0      |

### 2. **AND (Conjunción)**
La puerta lógica **AND** da una salida de `1` solo si ambas entradas son `1`. En cualquier otro caso, la salida es `0`.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/AND.png?raw=true)

| Entrada (A) | Entrada (B) | Salida (A AND B) |
|:-----------:|:-----------:|:----------------:|
|      0      |      0      |        0         |
|      0      |      1      |        0         |
|      1      |      0      |        0         |
|      1      |      1      |        1         |

### 3. **OR (Disyunción)**
La puerta lógica **OR** da una salida de `1` si al menos una de las entradas es `1`. Solo da `0` cuando ambas entradas son `0`.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/OR.png?raw=true)

| Entrada (A) | Entrada (B) | Salida (A OR B) |
|:-----------:|:-----------:|:---------------:|
|      0      |      0      |       0         |
|      0      |      1      |       1         |
|      1      |      0      |       1         |
|      1      |      1      |       1         |

### 4. **XOR (Disyunción exclusiva)**
La puerta lógica **XOR** da una salida de `1` solo si las entradas son diferentes. Si ambas entradas son iguales, la salida es `0`.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/XOR.png?raw=true)

| Entrada (A) | Entrada (B) | Salida (A XOR B) |
|:-----------:|:-----------:|:----------------:|
|      0      |      0      |        0         |
|      0      |      1      |        1         |
|      1      |      0      |        1         |
|      1      |      1      |        0         |

### 5. **MUX (Multiplexor)**
Un **MUX** selecciona una de varias entradas de datos en función de las señales de selección y la envía como salida.

Para un MUX de 2 a 1 (una señal de selección `S`):

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica1_Logica_Booleana/Imagenes/MUX.png?raw=true)

| Entrada (A) | Entrada (B) | Selección (S) | Salida (Y) |
|:-----------:|:-----------:|:-------------:|:----------:|
|      0      |      0      |       0       |     0      |
|      0      |      1      |       0       |     0      |
|      1      |      0      |       1       |     0      |
|      1      |      1      |       1       |     1      |

### 6. **DMUX (Demultiplexor)**
Un **DMUX** dirige una entrada a una de varias salidas, en función de las señales de selección.

Para un DMUX de 1 a 2 (una señal de selección `S`):

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

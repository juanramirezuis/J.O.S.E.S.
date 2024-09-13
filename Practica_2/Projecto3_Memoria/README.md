# J.O.S.E.S.
## Práctica 2: Proyecto 3: Memoria

### 1. **Bit**
El objetivo del **Bit** es almacenar un único valor binario (0 o 1) en la memoria y dejar que ese valor se actualice o se mantenga en función de una señal de control de entrada. Esto forma la base del 
almacenamiento en memoria mediante el uso de un flip-flop (DFF) como elemento principal. El DFF emite continuamente el valor almacenado y, cuando se lo indica la señal de control, actualiza su valor en función de una 
nueva entrada. Esto hace posible el funcionamiento de la memoria dinámica, lo que permite que el bit actúe como un bloque de construcción fundamental para unidades de memoria más complejas, como los registros y la RAM.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_2/Projecto3_Memoria/Imagenes/Bit.png)

### 2. **Register**
El objetivo del **Register** es almacenar un valor de 16 bits, lo que permite el almacenamiento y la recuperación de datos binarios en cantidades mayores que las que proporciona un solo bit. 
Funciona apartir de el uso de circuitos de muchos bits, donde cada bit almacena una parte del valor de varios bits. El registro permite que todo el valor de 16 bits se actualice al mismo tiempo o que permanezca sin 
cambios según la señal de control (carga). Los registros son fundamentales para almacenar datos, direcciones e instrucciones, lo que permite el manejo de datos de estilo binario de manera rapida y eficiente.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_2/Projecto3_Memoria/Imagenes/Block-diagram-of-4-bit-PIPO-Shift-register-using-D-Flip-Flop.png)

## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [From NAND To Tetris, Part 5: RAM, Memory, and Sequential Logic](https://www.youtube.com/watch?v=3xIQDyutc2Y&list=PLu6SHDdOToSdD4-c9nZX2Qu3ZXnNFocOH&index=8)
 - [NAND To Tetris 5a: Creating RAM and Memory lab](https://www.youtube.com/watch?v=lo54MEu7u9A&list=PLu6SHDdOToSdD4-c9nZX2Qu3ZXnNFocOH&index=9)

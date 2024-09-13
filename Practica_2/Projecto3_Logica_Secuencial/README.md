# J.O.S.E.S.
## Práctica 2: Proyecto 3: Logica Secuencial

### 1. **Bit**
El objetivo del **Bit** es almacenar un único valor binario (0 o 1) en la memoria y dejar que ese valor se actualice o se mantenga en función de una señal de control de entrada. Esto forma la base del 
almacenamiento en memoria mediante el uso de un flip-flop (DFF) como elemento principal. El DFF emite continuamente el valor almacenado y, cuando se lo indica la señal de control, actualiza su valor en función de una 
nueva entrada. Esto hace posible el funcionamiento de la memoria dinámica, lo que permite que el bit actúe como un bloque de construcción fundamental para unidades de memoria más complejas, como los registros y la RAM.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_2/Projecto3_Logica_Secuencial/Imagenes/Bit.png)

### 2. **Register**
El objetivo del **Register** es almacenar un valor de 16 bits, lo que permite el almacenamiento y la recuperación de datos binarios en cantidades mayores que las que proporciona un solo bit. 
Funciona apartir de el uso de circuitos de muchos bits, donde cada bit almacena una parte del valor de varios bits. El registro permite que todo el valor de 16 bits se actualice al mismo tiempo o que permanezca sin 
cambios según la señal de control (carga). Los registros son fundamentales para almacenar datos, direcciones e instrucciones, lo que permite el manejo de datos de estilo binario de manera rapida y eficiente.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_2/Projecto3_Logica_Secuencial/Imagenes/Block-diagram-of-4-bit-PIPO-Shift-register-using-D-Flip-Flop.png)


### 3. **PC (Program Counter)**
Está diseñado para mantener un valor de 16 bits que puede ser incrementado, cargado con un valor externo o reseteado. El chip puede realizar tres operaciones principales:

- Incrementar: Si la señal inc está activa, el valor actual del contador se incrementa en 1.
- Cargar: Si la señal load está activa, el valor en el bus de entrada in[16] se carga en el contador.
- Resetear: Si la señal reset está activa, el contador se reinicia a 0.

Estas operaciones son controladas mediante el flujo de datos a través de los diferentes multiplexores, que seleccionan el valor adecuado (incrementado, cargado o reseteado) antes de almacenarlo en el registro.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_2/Projecto3_Logica_Secuencial/Imagenes/pc.png?raw=true)

### 4. **RAM4K**
Es una memoria RAM de 4K (4096) direcciones, donde cada dirección almacena un dato de 16 bits. El chip puede dividir la memoria en 8 bloques más pequeños, donde cada bloque puede almacenar hasta 512 palabras de 16 bits. Su funcionamiento es: 

- El demultiplexor DMux8Way toma los 3 bits más significativos de la dirección y decide cuál de los 8 bloques de RAM debe habilitarse para almacenar el valor en función de la señal de carga load.
- Cada uno de los bloques RAM512 se encarga de manejar una sub-sección de 512. Los 9 bits menos significativos de la dirección determinan qué valor específico dentro de ese bloque se lee o escribe.
- El multiplexor Mux8Way16 selecciona cuál de los 8 bloques de RAM proporciona el valor de salida, según los 3 bits más significativos de la dirección.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_2/Projecto3_Logica_Secuencial/Imagenes/ram4k.jpg?raw=true)

### 5. **RAM16K**
Es una memoria RAM de 16K (16384) direcciones, donde cada dirección almacena un valor de 16 bits. Su funcionamiento es: 

- El demultiplexor DMux4Way toma los 2 bits más significativos de la dirección y decide cuál de los 4 bloques de RAM debe habilitarse para almacenar un valor en función de la señal de carga load.
- Cada uno de los bloques RAM4K se encarga de manejar una sub-sección de 4096. Los 12 bits menos significativos de la dirección determinan qué palabra específica dentro de ese bloque se lee o escribe.
- El multiplexor Mux4Way16 selecciona cuál de los 4 bloques de RAM proporciona el valor de salida, según los 2 bits más significativos de la dirección.

![alt text](https://github.com/juanramirezuis/J_O_S_E_S/blob/main/Practica_2/Projecto3_Logica_Secuencial/Imagenes/ram16k.png?raw=true)

## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [From NAND To Tetris, Part 5: RAM, Memory, and Sequential Logic](https://www.youtube.com/watch?v=3xIQDyutc2Y&list=PLu6SHDdOToSdD4-c9nZX2Qu3ZXnNFocOH&index=8)
 - [NAND To Tetris 5a: Creating RAM and Memory lab](https://www.youtube.com/watch?v=lo54MEu7u9A&list=PLu6SHDdOToSdD4-c9nZX2Qu3ZXnNFocOH&index=9)

Imagenes:
 - https://nand2tetris-hdl.github.io/img/pc.png
 - https://youtu.be/yk8OCAmytHM?si=h3O2IdQ7-irpckD6
 - https://nand2tetris-hdl.github.io/img/ram8.png

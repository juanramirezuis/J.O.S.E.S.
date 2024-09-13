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

### 6. **RAM8**
La RAM8 es una unidad de memoria que puede almacenar 8 palabras de 16 bits cada una. Está construida a partir de registros de 16 bits y se utiliza en sistemas de cómputo para almacenar datos temporalmente. Aquí te explico en detalle cómo funciona y cómo se implementa en el contexto de Nand2Tetris usando el lenguaje de descripción de hardware (HDL):

**1. Componentes principales de la RAM8:**

**•	8 registros de 16 bits:** Cada registro puede almacenar una palabra de 16 bits. Esto significa que la RAM8 puede almacenar un total de 8 palabras.

**•	Multiplexores (MUX):** Los multiplexores son usados para seleccionar cuál de los registros debe leer o escribir, dependiendo de la dirección que se reciba.

**•	Decodificador:** Este se usa para habilitar el registro correcto durante una operación de escritura.


**2. Entradas de la RAM8:**

**•	in[16]:** Entrada de datos de 16 bits. Es el valor que quieres almacenar en uno de los registros de la RAM.

**•	address[3]:** Es la dirección de 3 bits que determina cuál de los 8 registros se va a seleccionar para leer o escribir. Un valor de 3 bits puede representar un total de 23=82^3 = 823=8 combinaciones, por lo que se pueden direccionar los 8 registros.

**•	load:** Esta señal es un bit que indica si se debe almacenar (cargar) el valor de in en el registro seleccionado. Si load = 1, el valor de la entrada in se almacenará en el registro correspondiente a la dirección dada por address.

**•	clk (clock):** La señal de reloj controla cuándo se debe realizar la operación de escritura en el registro seleccionado.


**3. Salida de la RAM8:**

**•	out[16]:** La salida es de 16 bits y corresponde al valor almacenado en el registro seleccionado por la dirección address.

**4. Funcionamiento detallado:**

**•	Lectura:** Cuando la señal de load es 0, la RAM8 no cambia el valor almacenado en sus registros. La salida será el valor almacenado en el registro indicado por address.

**•	Escritura:** Si la señal load es 1, la RAM8 toma el valor de in y lo almacena en el registro indicado por la dirección address. Esto sucede al pulso del reloj (en la transición de bajo a alto de la señal clk).

**•	Decodificación y selección de registro:**

-Para la operación de escritura, el decodificador toma los 3 bits de la dirección y habilita uno de los 8 registros. El valor de in se almacenará solo en el registro habilitado.

-Para la operación de lectura, un multiplexor selecciona el valor almacenado en el registro que corresponde a la dirección, y lo saca por la señal out.

**5. Explicación del HDL:**

**•	Registros:** Se definen 8 registros de 16 bits con la instrucción Register.

**•	DMux8Way:** Este desmultiplexor toma la señal load y, dependiendo de la dirección (address), habilita la escritura en uno de los 8 registros.

**•	Mux8Way16:** El multiplexor de 8 vías selecciona uno de los 8 registros para leer su contenido, de acuerdo a la dirección address, y envía el valor a la salida out.

### 7. **RAM64**

La RAM64 es una extensión de la RAM8, diseñada para almacenar 64 palabras de 16 bits cada una. En el contexto de Nand2Tetris, la RAM64 se construye utilizando 8 instancias de RAM8. Aquí te explico en detalle cómo funciona y cómo se implementa en HDL (Hardware Description Language).

1. Componentes principales de la RAM64:

•	8 bloques de RAM8: La RAM64 está formada por 8 unidades de RAM8, donde cada bloque almacena 8 palabras de 16 bits.

•	Multiplexores (MUX): Se utilizan multiplexores para seleccionar de cuál bloque de RAM8 leer o escribir.

•	Decodificador: Un decodificador decide cuál de las RAM8 debe habilitarse para una operación de escritura.

2. Entradas de la RAM64:

•	in[16]: Entrada de datos de 16 bits, el valor que deseas almacenar en la RAM64.

•	address[6]: Una dirección de 6 bits que se usa para seleccionar tanto el bloque de RAM8 como el registro dentro de ese bloque. La dirección de 6 bits permite acceder a 26=642^6 = 6426=64 posiciones de memoria.

-Los primeros 3 bits de address seleccionan cuál de las 8 RAM8 se debe usar (por eso tenemos 8 bloques).

-Los últimos 3 bits de address seleccionan cuál de los 8 registros dentro del bloque de RAM8 se debe leer o escribir.

•	load: Señal de 1 bit que indica si se debe cargar (escribir) el valor de in en la posición seleccionada de la RAM64.

•	clk (clock): Señal de reloj que sincroniza las operaciones de escritura en los registros.

3. Salida de la RAM64:

•	out[16]: La salida es de 16 bits y contiene el valor almacenado en la posición de memoria seleccionada por address.

4. Funcionamiento detallado:

•	Decodificación de la dirección:

-Los primeros 3 bits de address (bits más significativos) seleccionan cuál de las 8 RAM8 manejará la operación. Esta selección se hace mediante un desmultiplexor de 8 vías (DMux8Way).

-Los últimos 3 bits de address se pasan a cada una de las RAM8 para que seleccionen cuál de los registros dentro de la RAM8 debe manejar la operación de lectura o escritura.

•	Escritura: Si la señal load es 1, la RAM64 toma el valor de in y lo almacena en el registro seleccionado. Solo el bloque de RAM8 correspondiente (según los 3 bits más significativos) 

podrá recibir el valor de in y cargarlo en el registro correcto (seleccionado por los 3 bits menos significativos).

•	Lectura: Cuando load = 0, la RAM64 no cambia ningún valor almacenado. El valor de salida out será el valor almacenado en el registro seleccionado por la dirección.

5. Explicación del HDL:

•	RAM8: Se instancian 8 bloques de RAM8, cada uno manejando un conjunto de 8 palabras de 16 bits.

•	address[3..5]: Los bits 3, 4 y 5 del address (los 3 bits menos significativos) se pasan a las RAM8 para seleccionar qué registro dentro de cada RAM8 debe operar.

•	DMux8Way: Este desmultiplexor toma la señal load y, dependiendo de los bits 0, 1 y 2 de address (los 3 bits más significativos), habilita la carga en uno de los 8 bloques de RAM8.

•	Mux8Way16: Este multiplexor selecciona la salida del bloque de RAM8 que corresponde a los bits 0, 1 y 2 de address.

### 8. **RAM512**

La RAM512 es una unidad de memoria que almacena 512 palabras de 16 bits cada una, y se construye como una extensión de la RAM64. En el contexto de Nand2Tetris, se logra utilizando 8 instancias de RAM64, de forma similar a cómo se construye la RAM64 a partir de bloques de RAM8.

1. Componentes principales de la RAM512:

•	8 bloques de RAM64: La RAM512 está compuesta por 8 bloques de RAM64. Cada bloque almacena 64 palabras de 16 bits, lo que da un total de 8×64=5128 \times 64 = 5128×64=512 palabras.

•	Multiplexores (MUX): Se usan multiplexores para seleccionar el bloque de RAM64 adecuado de donde leer o escribir.

•	Decodificador: Un desmultiplexor selecciona cuál de las 8 RAM64 debe habilitarse para la operación de escritura.

2. Entradas de la RAM512:

•	in[16]: Entrada de datos de 16 bits, el valor que se quiere almacenar en la RAM512.

•	address[9]: Dirección de 9 bits que indica qué posición de memoria acceder en la RAM512.

-Los primeros 3 bits del address se usan para seleccionar uno de los 8 bloques de RAM64.

-Los últimos 6 bits del address se usan para seleccionar cuál registro dentro del bloque de RAM64 debe ser leído o escrito.

•	load: Señal de control de 1 bit que indica si se debe almacenar el valor de in en la posición de memoria seleccionada.

•	clk (clock): Señal de reloj que sincroniza la operación de escritura en los registros.

•	3. Salida de la RAM512:

•	out[16]: La salida es de 16 bits y contiene el valor almacenado en la posición de memoria seleccionada.

•	4. Funcionamiento detallado:

•	Decodificación de la dirección:

-Los primeros 3 bits de address (bits más significativos) seleccionan cuál de los 8 bloques de RAM64 debe manejar la operación de lectura o escritura. Esto se realiza mediante un desmultiplexor de 8 vías (DMux8Way).

-Los últimos 6 bits de address (bits menos significativos) se pasan a los bloques de RAM64. Estos 6 bits se dividen en dos partes:
Los 3 bits más significativos de esta parte seleccionan cuál de los 8 registros dentro del bloque RAM64 debe ser utilizado (función de RAM8 dentro de la RAM64).
Los 3 bits menos significativos se pasan dentro de los bloques de RAM8.

•	Escritura: Si load es 1, el valor en in se almacena en la posición de memoria correspondiente. Solo el bloque de RAM64 seleccionado y el registro dentro de ese bloque reciben el valor de in y lo almacenan.

•	Lectura: Si load es 0, se mantiene el valor de la memoria. La salida out será el valor almacenado en el registro correspondiente a la dirección address.

5. Explicación del HDL:

•	RAM64: Se instancian 8 bloques de RAM64, cada uno manejando 64 palabras de 16 bits.

•	address[3..8]: Los bits 3 a 8 de la dirección se pasan a los bloques RAM64, los cuales gestionan internamente la selección de los registros adecuados.

•	DMux8Way: Este desmultiplexor toma la señal load y, dependiendo de los bits 0, 1 y 2 de address, habilita la escritura en uno de los 8 bloques de RAM64.

•	Mux8Way16: El multiplexor selecciona la salida del bloque RAM64 correspondiente según los bits 0, 1 y 2 de address, que determinan de cuál bloque de RAM64 se obtendrá la salida.


## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [From NAND To Tetris, Part 5: RAM, Memory, and Sequential Logic](https://www.youtube.com/watch?v=3xIQDyutc2Y&list=PLu6SHDdOToSdD4-c9nZX2Qu3ZXnNFocOH&index=8)
 - [NAND To Tetris 5a: Creating RAM and Memory lab](https://www.youtube.com/watch?v=lo54MEu7u9A&list=PLu6SHDdOToSdD4-c9nZX2Qu3ZXnNFocOH&index=9)

Imagenes:
 - https://nand2tetris-hdl.github.io/img/pc.png
 - https://youtu.be/yk8OCAmytHM?si=h3O2IdQ7-irpckD6
 - https://nand2tetris-hdl.github.io/img/ram8.png

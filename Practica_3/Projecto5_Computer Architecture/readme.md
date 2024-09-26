# J.O.S.E.S.
## Práctica 3:.


# Memory


El archivo `Memory.hdl` define el chip de memoria del ordenador dentro del proyecto 5 de "Nand to Tetris". Este chip encapsula toda la lógica necesaria para gestionar la memoria del computador, que incluye tanto la memoria RAM como los dispositivos de memoria mapeada de entrada/salida (I/O). Se diseñó para permitir operaciones de lectura y escritura, asegurando que los datos se manejen de manera eficiente y conforme a las reglas del espacio de direcciones especificadas.

### Descripción Técnica
El chip de memoria está configurado para interactuar con la memoria RAM, la pantalla (Screen) y el teclado (Keyboard), usando múltiples componentes de desmultiplexación (`DMux`) y multiplexación (`Mux16`). 

Aqui podemos ver su implementación:

![image](https://github.com/user-attachments/assets/777c0845-38e4-4759-98a7-f758460c3c25)


1. **Entradas y Salidas:**
   - `in[16]`: Representa el dato a escribir en la memoria.
   - `load`: Un señal de control que indica si se debe escribir el dato.
   - `address[15]`: Dirección de memoria a la que se accede para leer o escribir.
   - `out[16]`: Salida del dato leído de la dirección especificada.

2. **Manejo de la Dirección y Mapeo de Memoria:**
   - Las direcciones se manejan a través de múltiples `DMux` para dirigir la señal de `load` hacia la memoria RAM o los dispositivos (pantalla y teclado) basados en los bits más significativos de la dirección (bits 14 y 13).
   - `RAM16K`: Se encarga del almacenamiento principal, manejando las direcciones de 0x0000 a 0x3FFF.
   - `Screen`: Gestiona el mapa de memoria de la pantalla, activo en el rango de direcciones de 0x4000 a 0x5FFF.
   - `Keyboard`: Controla la entrada del teclado, mapeado a la dirección 0x6000.

3. **Lógica de Multiplexación:**
   - `Mux16`: Se utilizan para seleccionar la salida adecuada basada en la dirección, priorizando la salida de dispositivos sobre la RAM cuando es necesario. Esto asegura que cualquier acceso a direcciones específicas resulte en la salida correcta, ya sea de la RAM, la pantalla o el teclado.


# CPU


El archivo `CPU.hdl` define el diseño de la CPU, que se encargará de ejecutar las instrucciones almacenadas en la memoria y de coordinar todas las operaciones de procesamiento. 

### Descripción Técnica

![image](https://github.com/user-attachments/assets/f0d0a4db-aace-4e18-9f43-5d2f9d2bbdd5)

1. **Entradas y Salidas de la CPU:**

   - `inM[16]`: La entrada que proviene de la memoria (el valor almacenado en la dirección de memoria actual).
   - `instruction[16]`: La instrucción actual que se debe ejecutar.
   - `reset`: Señal que reinicia la CPU.
   - `outM[16]`: Salida de la CPU, el valor que debe escribirse en memoria.
   - `writeM`: Señal de control que indica si debe escribirse el valor de salida en la memoria.
   - `addressM[15]`: Dirección de memoria que se está leyendo o escribiendo.
   - `pc[15]`: Contador del programa, que indica la instrucción siguiente a ejecutar.
     
2. **Componentes Clave:**
- `ALU (Unidad Aritmético-Lógica)`: Se encarga de realizar operaciones aritméticas y lógicas basadas en las instrucciones recibidas.
- `Registros A y D`: El registro A almacena direcciones o valores de datos, y el registro D es el registro de datos.
- `Control de flujo`: Se maneja el flujo del programa a través del contador de programa (PC), que puede ser incrementado, reiniciado o cargado con una nueva dirección en caso de saltos condicionales o incondicionales.
  
3. **Lógica de Control:**
El archivo HDL debe implementar la lógica para decodificar el tipo de instrucción (A-instruction o C-instruction), y determinar si se debe ejecutar un salto, realizar una operación en la ALU, o manejar datos de la memoria.


# Computer
La parte de Computer en el Proyecto 5 de Nand2Tetris se refiere a la construcción y prueba de una computadora básica basada en la arquitectura del Hack computer. Esta computadora tiene una CPU simple, memoria, y la capacidad de ejecutar programas escritos en su propio lenguaje de máquina.

![image](https://github.com/user-attachments/assets/6f34bbdf-6145-4b52-8c79-0637246c3aa4)

1. **Arquitectura General del Hack Computer**
El Hack Computer es un sistema de computación completo que se basa en los siguientes componentes principales:

- Unidad Aritmético-Lógica (ALU): Realiza operaciones aritméticas y lógicas.
- Registro A: Almacena valores que pueden ser usados para direcciones de memoria o para cálculos.
- Registro D: Utilizado exclusivamente para operaciones aritméticas.
- Memoria: Incluye tanto la RAM como el Registro M (una vista en la RAM).
- Programa Counter (PC): Guarda la dirección de la instrucción actual en ejecución.

2. **Construcción del Computer**
El proyecto guía en la construcción de la CPU, que integra la ALU, los registros, y la lógica de control. Esta CPU se combina luego con la memoria y el programa counter para formar la computadora completa.

3. **Programas de Prueba:** ComputerAdd y ComputerRect
Los programas de prueba proporcionados (ComputerAdd y ComputerRect) se utilizan para verificar que la computadora que has construido funcione correctamente. 

**ComputerAdd:**
Este programa simple realiza la suma de dos números y almacena el resultado en la memoria. Verifica la funcionalidad básica de la ALU y la interacción entre los registros y la memoria.

**ComputerRect:**
Este programa dibuja un rectángulo en la pantalla, lo que prueba no solo las operaciones aritméticas, sino también las capacidades de control de flujo y acceso a la memoria en la computadora Hack.

4. **Archivos de Prueba y Comparación**

- **Archivos .tst:**
Estos son archivos de prueba que contienen las instrucciones para ejecutar los programas en tu computadora Hack y observar los resultados. Incluyen secuencias de instrucciones y configuraciones que tu implementación debe ejecutar.
- **Archivos .cmp:**
Estos son archivos de comparación que contienen los resultados esperados de la ejecución de las pruebas. Cuando corres una prueba, tu computadora Hack genera una salida que se compara automáticamente con el archivo .cmp para verificar si la implementación es correcta.

6. **Proceso de Prueba**
Para probar tu computadora:
Ejecutas el archivo .tst en el simulador.
El simulador carga y ejecuta el programa en la computadora Hack que se construyo.
Los resultados se comparan con los valores esperados en el archivo .cmp.

La implementación usa un enfoque modular para manejar diferentes áreas de memoria, lo que facilita el mantenimiento y la escalabilidad del sistema. Al separar claramente la lógica para cada tipo de memoria y utilizar componentes de des/multiplexación, el diseño asegura que las operaciones de memoria sean rápidas y eficientes, reduciendo la complejidad y mejorando la claridad del sistema de memoria global, además, este diseño permite una gestión eficiente y efectiva del espacio de memoria del computador, proporcionando un acceso claro y estructurado a la RAM y a los dispositivos de I/O mapeados. 


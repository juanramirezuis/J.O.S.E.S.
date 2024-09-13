# J.O.S.E.S.

## Práctica 2: Proyectos 2 y 3.

## 1. ¿Cuál es el objetivo de cada uno de esos proyectos con sus palabras y describa que debe hacer para desarrollarlo?

### Objetivo del Proyecto 2 (Lógica Aritmética):
Este proyecto se centra en diseñar y construir componentes fundamentales para la aritmética y la lógica digital, por lo cual su objetivo es desarrollar circuitos que realicen operaciones básicas, como la suma de 
bits y la manipulación de números de 16 bits, y luego integrar estos componentes en una Unidad Aritmética y Lógica (ALU) capaz de realizar diversas operaciones aritméticas y lógicas. Esto incluye la creación de 
sumadores simples y avanzados, un incrementador de 16 bits y, finalmente, una ALU que pueda ejecutar y gestionar diferentes tipos de operaciones según las instrucciones de control.

**Desarrollo:**

Para alcanzar este objetivo, primero diseñamos circuitos básicos como el Half Adder y el Full Adder, que son los bloques fundamentales para realizar sumas de bits. Luego se construyo un sumador de 16 bits (Add16) y 
un incrementador de 16 bits (Inc16) utilizando estos adders básicos. Posteriormente, integramos estos componentes en una ALU que pueda realizar una variedad de operaciones aritméticas y lógicas, como suma, resta, 
AND y OR. La ALU debia incluir una lógica de control para seleccionar la operación deseada y proporcionar resultados correctos, así como señales de carry y zero según corresponda. Finalmente, realizamos pruebas de 
cada componente y del sistema completo para garantizar que todo funcione correctamente y cumpla con los requisitos especificados.


### Objetivo del Proyecto 3 (Lógica Secuencial):

Este proyecto tiene como objetivo construir la unidad de memoria del computador, la cual es indispensable para almacenar y acceder a datos durante la ejecución de programas. A través del diseño de 
componentes secuenciales como registros, RAM de diferentes tamaños y el contador de programa (PC).

**Desarrollo:**

Para el desarrollo de este proyecto, se implementaron varios componentes secuencialesde memoria, comenzando con un bit utilizando flip-flops, luego un registro de 16 bits para almacenas palabras completas de datos, 
y posteriormente se desarrollan módulos de RAM de diferentes tamaños (RAM8, RAM64, RAM512, etc.) que permiten almacenar datos en direcciones específica, y finalmente, se construye el contador de programa (PC), que 
gestiona el flujo de ejecución de instrucciones. Todos estos componentes son diseñados en .hdl y se prueban en el simulador de hardware para comprobar que todo funcione y cumpla con los requisitos especificados.

## 2. Explique las principales diferencias entre la lógica aritmética y la lógica secuencial:
   
   La lógica aritmética (lógica combinacional) realiza operaciones como la suma, la resta y la manipulación bit a bit, y sus resultados dependen únicamente de las entradas actuales, sin recordar estados anteriores.
   Calcula los resultados instantáneamente, sin depender de entradas anteriores o de una señal de reloj. Por el contrario, la lógica secuencial almacena información y sus resultados dependen tanto de las entradas
   actuales como de los estados anteriores. Por lo general, está controlada por una señal de reloj, que dicta cuándo se deben actualizar los valores almacenados (memoria). Mientras que la lógica aritmética se
   utiliza en componentes como la unidad lógica aritmética (ALU) para cálculos inmediatos, la lógica secuencial es esencial para elementos de memoria como interruptores de flotador, registros y contadores, que
   rastrean el estado a lo largo del tiempo.

## PREGUNTA BONUS
   ¿Qué tipo de unidades aritmético lógicas existen?:

   Las unidades aritmético-lógicas (ALU) son componentes fundamentales en la arquitectura de una CPU. Estas unidades realizan operaciones aritméticas (como suma, resta) y lógicas (como AND, OR) sobre datos.
   
   La ALU se compone básicamente de: Circuito Operacional, Registros de Entradas, Registro Acumulador y un Registro de Estados, conjunto de registros que hacen posible la realización de cada una de las operaciones.
   
   La mayoría de las acciones de la computadora son realizadas por la ALU. La ALU toma datos de los registros del procesador. Estos datos son procesados y los resultados de esta operación se almacenan en los            registros de salida de la ALU. Otros mecanismos mueven datos entre estos registros y la memoria.
   
   Una unidad de control controla a la ALU, al ajustar los circuitos que le señala a la ALU qué operaciones realizar.
   
   Algunos tipos de ALU que existen, en función de su complejidad y diseño:
   
      1. ALU Combinacional:
         Esta es la forma más básica de ALU, donde la salida depende sólo de las entradas actuales, sin almacenar ningún estado. No tiene registros internos.
         Características:
            Realiza operaciones simples como suma, resta, AND, OR, XOR.
            Se usa en sistemas básicos y pequeños dispositivos embebidos.
            
      2. ALU con Acumulador:
         Utiliza un registro llamado "acumulador" para almacenar uno de los operandos y el resultado de las operaciones.
         Características:
            Es más eficiente para realizar múltiples operaciones sucesivas sobre un solo valor.
            Se emplea en procesadores de arquitectura antigua o sencilla.
            
      3. ALU Compleja o Multioperativa:
         Es capaz de realizar operaciones más avanzadas, como multiplicaciones y divisiones, además de operaciones lógicas y aritméticas básicas.
         Características:
            Integra instrucciones aritméticas avanzadas (como multiplicaciones de enteros de gran tamaño).
            Se usa en procesadores modernos para mejorar la eficiencia en cálculos matemáticos complejos.
            
      4. ALU Escalar:
         Realiza una única operación sobre un par de operandos a la vez.
         Características:
            Adecuada para procesadores sencillos que no requieren ejecutar múltiples instrucciones en paralelo.
            
      5. ALU Vectorial o SIMD (Single Instruction, Multiple Data):
         Capaz de realizar operaciones en paralelo sobre múltiples datos, es decir, un solo conjunto de instrucciones se ejecuta en varios datos simultáneamente.
         Características:
            Usada en procesadores gráficos (GPU) o sistemas orientados al procesamiento de grandes volúmenes de datos (como cálculos científicos).
            Mejora el rendimiento en tareas que requieren cálculos masivos en paralelo.
            
      6. ALU Especializada:
         Diseñada para aplicaciones específicas como procesamiento de señales digitales (DSP) o algoritmos criptográficos.
         Características:
            Optimizada para operaciones especializadas como el cálculo de transformadas rápidas de Fourier (FFT) o encriptación.
            Se encuentra en dispositivos de alta especialización.
            
      7. ALU de Punto Flotante:
         Este tipo de ALU realiza operaciones sobre números en formato de punto flotante, que permiten representar una gama más amplia de valores con mayor precisión que los enteros.
         Características:
            Crucial en aplicaciones científicas y de gráficos que requieren alta precisión matemática.
            Se encuentra en procesadores de alto rendimiento.
            
   Cada tipo de ALU se usa en diferentes contextos, dependiendo de los requerimientos del sistema en términos de velocidad, precisión y tipo de operaciones que se deben realizar.

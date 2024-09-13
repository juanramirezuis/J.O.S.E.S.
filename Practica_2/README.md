# J.O.S.E.S.
## Práctica 2: Logica Booleana.

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

## Bibliografia
Esta practica fue resuelta apoyandonos del siguiente material:
 - [From NAND To Tetris - Logic Gates Lab](https://www.youtube.com/watch?v=Mzy0RG9Z1Ak&t=78s)
Imagenes:
 - https://circuitdigest.com/sites/default/files/inlineimages/u/4-to-1-MUX-using-three-2-to-1-MUX.png
 - https://www.electronicshub.org/wp-content/uploads/2021/04/Block-Diagram-of-16-to-1-Multiplexer.jpg
 - https://d2vlcm61l7u1fs.cloudfront.net/media%2F268%2F26880fba-979c-4637-b9c2-d2da3aae7580%2FphpHS1AKM.png

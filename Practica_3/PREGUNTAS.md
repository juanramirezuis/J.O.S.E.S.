# J.O.S.E.S.

## Práctica 2: Proyectos 2 y 3.

## 1.	¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?

El lenguaje de máquina es fundamental para definir la arquitectura computacional, ya que es el único que el procesador puede comprender y ejecutar de manera directa sin requerir traducción, este lenguaje está formado por instrucciones codificadas en secuencias de bits que el hardware interpreta para realizar operaciones específicas, como el movimiento de datos o la realización de cálculos. El diseño de un procesador se basa en el conjunto de instrucciones que puede ejecutar, conocido como ISA (Instruction Set Architecture), lo que determina cómo interactúa con la memoria y otros dispositivos, además, la relación entre el lenguaje de máquina y la arquitectura permite optimizar el rendimiento del sistema, ya que las instrucciones están diseñadas para maximizar la eficiencia del hardware, asimismo, el conjunto de instrucciones garantiza la compatibilidad del software con la arquitectura, influyendo en su portabilidad entre distintas plataformas, por ende, el lenguaje de máquina es esencial para definir la estructura y funcionamiento básico de un sistema computacional.


## 2.	¿Qué diferencia ven entre arquitectura computacional, arquitectura de software y arquitectura del sistema? Justifique su respuesta.
   
Desde nuestro punto de vista, la arquitectura computacional, la arquitectura de software y la arquitectura del sistema representan tres niveles de diseño que, aunque relacionados, abordan aspectos diferentes de un sistema tecnológico. La arquitectura computacional establece las bases del hardware, la arquitectura de software organiza cómo funcionará el software sobre ese hardware, y la arquitectura del sistema define cómo todos los componentes, tanto físicos como lógicos, interactúan en conjunto para crear un sistema cohesionado. Cada una tiene su relevancia, pero abarcan distintos niveles de complejidad y abstracción.

La **arquitectura computacional** se enfoca en el diseño del hardware, principalmente cómo interactúan los componentes físicos de una computadora como el procesador, la memoria y los buses. Es el "esqueleto" que define qué instrucciones puede ejecutar la máquina y cómo se comunican los componentes internos, esta es la capa más fundamental porque define los límites de lo que es posible en términos de procesamiento y rendimiento. 

La **arquitectura de software** se centra en la organización del software, cómo se estructura el código, los módulos y cómo interactúan entre sí dentro del sistema, aquí entra en juego el diseño de patrones y principios que aseguren que el software sea escalable, mantenible y eficiente, esto es crucial para garantizar que las aplicaciones no solo funcionen bien dentro de una computadora específica, sino que también puedan adaptarse y evolucionar a medida que cambian las necesidades.

La **arquitectura del sistema** integra tanto el hardware como el software, pero lo hace desde una perspectiva más amplia, abarcando la infraestructura general, como servidores, redes y la interacción entre varios subsistemas, creemos que esta es la visión más global, donde se consideran aspectos de seguridad, redundancia y escalabilidad a nivel de todo el ecosistema.



## PREGUNTA BONUS
  Como informático o computista: ¿La arquitectura computacional o la arquitectura del sistema no tiene en cuenta igualmente la arquitectura de software? Justifique su respuesta.

Consideramos que tanto la arquitectura computacional como la arquitectura del sistema toman en cuenta, aunque de manera diferente, la arquitectura de software, pero no en la misma medida ni con el mismo enfoque.

La arquitectura computacional no se preocupa directamente por cómo se estructura el software en términos de lógica, pero establece las capacidades y limitaciones que el software debe respetar, el software se desarrolla teniendo en cuenta las instrucciones que puede ejecutar el procesador (ISA), la cantidad de memoria disponible y cómo se gestionan los recursos de hardware. En este sentido, aunque no diseña el software, la arquitectura computacional lo condiciona profundamente. En contraste, la arquitectura del sistema sí tiene una visión más holística, considerando la interacción entre el hardware, el software y la infraestructura que los conecta, en este nivel, la arquitectura del sistema debe integrar cómo el software se desplegará y funcionará sobre los recursos físicos y lógicos. Aquí es donde se planifican aspectos como la seguridad, la redundancia, el rendimiento, y se toman decisiones basadas en cómo el software debe ejecutarse y comunicarse a través de diferentes máquinas y redes. 

En resumen, mientras que la arquitectura computacional influye en el software en cuanto a los recursos disponibles y las instrucciones que puede ejecutar, la arquitectura del sistema lo incorpora activamente en su diseño, considerando cómo interactúa con el hardware y con otros subsistemas, podemos decir que ambos enfoques lo tienen en cuenta, pero con diferentes grados de involucramiento.

![image](https://github.com/user-attachments/assets/b05ad884-6a9c-4dbe-bfcd-dd25d223df31)


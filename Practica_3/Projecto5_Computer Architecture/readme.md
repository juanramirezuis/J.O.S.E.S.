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


La implementación usa un enfoque modular para manejar diferentes áreas de memoria, lo que facilita el mantenimiento y la escalabilidad del sistema. Al separar claramente la lógica para cada tipo de memoria y utilizar componentes de des/multiplexación, el diseño asegura que las operaciones de memoria sean rápidas y eficientes, reduciendo la complejidad y mejorando la claridad del sistema de memoria global, además, este diseño permite una gestión eficiente y efectiva del espacio de memoria del computador, proporcionando un acceso claro y estructurado a la RAM y a los dispositivos de I/O mapeados. 


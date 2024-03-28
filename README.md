# conway's life game in python
### Juego de la vida conway
Duvan Felipe Pacheco Rodriguez
27/03/2024

**"El Juego de la Vida"** es un modelo matemático y un autómata celular creado por el matemático británico John Conway en 1970. Aunque se llama un juego, en realidad no tiene jugadores activos. En cambio, es un modelo que simula la evolución de células en una cuadrícula bidimensional, siguiendo reglas simples.

El juego se desarrolla en una cuadrícula infinita (aunque en la práctica se utiliza una cuadrícula finita) donde cada celda puede estar viva o muerta. La evolución del estado de cada célula en el siguiente paso de tiempo está determinada por el estado de las células vecinas según las siguientes reglas:

1. Cualquier célula viva con menos de dos células vivas adyacentes muere (por falta de población, como si fuera por soledad).
2. Cualquier célula viva con dos o tres células vivas adyacentes sobrevive para la próxima generación.
3. Cualquier célula viva con más de tres células vivas adyacentes muere (por exceso de población, como si fuera por superpoblación).
4. Cualquier célula muerta con exactamente tres células vivas adyacentes se convierte en una célula viva (por reproducción).

Estas reglas simples pueden dar lugar a patrones complejos y comportamientos interesantes, incluidos "planeadores" (gliders), "estabilidades" (stills), "osciladores" (oscillators), y otras estructuras que pueden interactuar entre sí. El juego de la vida ha sido objeto de estudio en campos como la matemática, la informática, la biología y la física, y ha demostrado ser útil para comprender conceptos como la complejidad emergente y los sistemas dinámicos.


![2448-6655-ane-34-86-179-gf4](https://github.com/dupachecor/conway-s-game-of-life/assets/72562179/dc83a399-cf5d-46b3-94b2-7fb337ac57c4)

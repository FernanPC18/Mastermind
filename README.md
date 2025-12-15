# MASTERMIND

## Historias de usuario

- El usuario pone una combinación de 4 colores de entre 6 colores distintos (los cuales pueden repetirse a lo largo del código)
- La máquina intenta adivinarlo enum máximo de 12 intentos
- Por cada solución, se ofrecerá una corrección mostrando información sobre cada color, con 8 posibles estados posibles para cada uno:
    - Del -4 al -1  no se acertaron ninguno de los colores ni su lugar.
    - El 0 se acertaron todos los colores pero ninguno está en su lugar.
    - Del 1 al 4 los colores y sus posiciones están acertados.
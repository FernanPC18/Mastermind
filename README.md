# MASTERMIND

## Indice
- [Manual](#manual)
    - [Instalación](#instalación)
    - [Uso](#uso)
- [Metodología](#metodología)  
    - [Historias de usuario](#historias-de-usuario)
- [Diseño](#diseño)
    - [Diagrama de componentes](#diagrama-de-componentes)
    - [Herramientas utlizadas](#herramientas-utilizadas)
- [Conclusión](#conclusión)
    - [Mejoras](#posibles-mejoras)
    - [Dificultades](#dificultades)


## Manual

### Instalación

1. Clona el proyecto: `git clone https://github.com/FernanPC18/Mastermind`
2. Instalamos uv:
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Linux/MacOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. Instalar las dependencias y preparar el entorno virual: `uv sync`

### Uso

Para ejecutar el proyecto: 
- Desde el entorno virtual: `uv run main.py`
- Con el entorno global: `python3 main.py`

## Metodología

En este proyecto intentamos usar pair programming y TDD.
Intentamos hacer TDD pero nos atascabamos mucho en cada caso test individualmente y no conseguiamos avanzar en el proyecto, por lo que dejamos los casos test para cuando tuviesemos código funcional y poder refactorizarlo.

Todo el proyecto esubimos haciendo pair programing, centrandonos en un modulo a la vez.


### Historias de usuario

- El usuario pone una combinación de 4 colores de entre 6 colores distintos (los cuales pueden repetirse a lo largo del código)
- Los colores a usar son:
    - Rojo
    - Verde
    - Azul
    - Amarillo
    - Rosa
    - Blanco
- La máquina intenta adivinarlo enum máximo de 12 intentos
- Por cada solución, se ofrecerá una corrección mostrando información sobre cada color, con 8 posibles estados posibles para cada uno:
    - Del 0 al 3  no se acertaron ninguno de los colores ni su lugar.
    - El 4 se acertaron todos los colores pero ninguno está en su lugar.
    - Del 5 al 8 los colores y sus posiciones están acertados.

## Diseño

### Diagrama de componentes

### Herramientas utilizadas

- __Python__:
    - __Pytest__: Framework para facilitar la creación de casos test.
    - __Pytest-sugar__: Herramienta para hacer más comodo el probar test.
- __Markdown__

## Conclusión

Hemos aplicado lo aprendido en los primeros 3 mesese de clases. Principalmente aprendimos el funcionamiento de algoritmos genéticos y asentamos mejor las bases de todo lo que dimos el trimestre anterior.

### Posibles mejoras

Las posibles mejoras son principalmente de eficiencia del código, de otra forma podría llegar a la solución en menos intentos. Por otro lado también podríamos mejorar la legibilidad del código.

### Dificultades

Principalmente las dificultades fueron al entender el algorítmo genético y como aplicarlo en el proyecto, especialmente los módulos de creacion de nueva población y de asignación de fitess, ya que daba problemas por valores duplicados.


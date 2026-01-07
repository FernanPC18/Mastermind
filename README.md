# MASTERMIND

## Indice
- [Instalación](#instalación)
- [Uso](#uso)
- [Historias de usuario](#historias-de-usuario)

## Instalación

1. Clona el proyecto: `git clone https://github.com/FernanPC18/Mastermind`
2. Instalamos uv:
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Linux/MacOS: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. Instalar las dependencias y preparar el entorno virual: `uv sync`

## Uso

Para ejecutar el proyecto: 
- Desde el entorno virtual: `uv run main.py`
- Con el entorno global: `python3 main.py`

## Historias de usuario

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
# Sistemas Continuos: Intercambio Térmico

## Descripción del Proyecto

Este software realiza la simulación numérica y el análisis del comportamiento de un **sistema de intercambio térmico acoplado entre dos cuerpos**. 

El modelo en estudio está compuesto por dos objetos con capacidades térmicas individuales, inmersos en un ambiente con temperatura constante ($T_{amb}$). La dinámica de transferencia de calor implementada contempla dos fenómenos simultáneos:

* **Transferencia con el entorno:** Cada cuerpo interactúa de forma independiente con el medio ambiente a través de sus respectivas fronteras.
* **Transferencia mutua (acoplamiento):** Existe un flujo térmico bidireccional entre ambos objetos generado por su contacto directo, donde el calor se desplaza desde el cuerpo de mayor temperatura hacia el de menor temperatura.

El objetivo principal de la simulación es resolver y evaluar la evolución temporal de las temperaturas de ambos cuerpos ($T_1$ y $T_2$) a partir de un conjunto de condiciones iniciales parametrizables, permitiendo estudiar visualmente la convergencia y el comportamiento del sistema.

# Autores

    Andreani, Manuel Francisco

    Gribaudo Re, Francisco Agustín

# Requisitos Previos
Para ejecutar esta simulación, asegúrate de contar con las siguientes dependencias instaladas en tu sistema:

    Python 3.x

    NumPy: Biblioteca fundamental para computación científica en Python.

        pip install numpy
    
    Gnuplot: Herramienta gráfica por línea de comandos. Puedes descargarla desde su sitio web oficial o instalarla mediante el gestor de paquetes de tu sistema operativo.

# Ejecución del Programa

Para poner en marcha la simulación, sigue estos pasos:

    Abre una terminal.

    Navega hasta el directorio raíz del proyecto.

    Ejecuta el script principal utilizando Python:

        python main.py

# Configuración de la Simulación

El comportamiento del sistema puede ser ajustado sin necesidad de modificar el código fuente. Para cambiar los parámetros de la simulación:

    - Localiza y abre el archivo parametros.txt en tu editor de texto preferido.

    - Modifica los valores según las necesidades de tu experimento.

    - Guarda los cambios.

    - Vuelve a ejecutar main.py para que la simulación tome los nuevos valores.
Proyecto: Modificaciones al Juego Cannon

Este repositorio contiene las modificaciones realizadas al clásico juego Cannon desarrollado con la librería freegames de Python.

📋 Descripción del Juego

El juego consiste en un cañón que dispara proyectiles rojos para impactar balones/objetivos azules que se desplazan desde la derecha de la pantalla hacia la izquierda.

👥 Trabajo de Integrantes

🚀 Integrante 1: Aumento de Velocidad

Objetivo: Incrementar la velocidad general del juego para hacer la experiencia más dinámica y desafiante.

Cambios implementados:

Velocidad de Objetivos (Balones):

Se modificó el desplazamiento horizontal en el bucle principal de -0.5 a -2.0 unidades por fotograma.

Velocidad Inicial del Proyectil:

Se ajustó la fórmula de cálculo del vector de velocidad en la función tap(x, y), cambiando el divisor de 25 a 12 para otorgar mayor impulso inicial.

Efecto de Gravedad / Velocidad Vertical:

Se incrementó el valor de la aceleración gravitatoria aplicada al proyectil de -0.35 a -0.7 unidades por fotograma.

♾️ Integrante 2: Modo Juego Infinito

Objetivo: Modificar la lógica para evitar el Game Over y lograr un bucle de juego continuo.

Cambios implementados:

Reposicionamiento de Objetivos:

En lugar de finalizar la partida cuando un balón sale del borde izquierdo (x < -200), el balón se reubica al extremo derecho (x = 200) asignándole una nueva coordenada vertical aleatoria (y).

Eliminación de Condición de Salida:

Se removió la condición de terminación if not inside(target): return en la función move(), permitiendo que el temporizador ontimer(move, 50) continúe indefinidamente.

💻 Requisitos e Instalación

Requisitos Previos

Python 3.x instalado.

Librerías Requeridas

Instalar la dependencia principal a través de pip:

pip install freegames


🎮 Ejecución del Juego

Para ejecutar cualquiera de las versiones, guarda el código correspondiente en un archivo .py (por ejemplo, cannon.py) y ejecútalo desde tu terminal:

python cannon.py


Controles

Clic Izquierdo: Dispara un proyectil desde la esquina inferior izquierda en dirección al punto seleccionado.

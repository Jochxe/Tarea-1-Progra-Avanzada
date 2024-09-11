# Preguntas Teóricas

**¿Qué es un paradigma de programación?**

Un paradigma de programación es un enfoque o estilo que define la forma en que se programa y se estructura el código.

**¿En qué se basa la programación orientada a objetos?**

La programación orientada a objetos se basa en organizar el software en torno a objetos, donde cada uno de estos posee atributos y acciones que puede realizar.

**¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación big *O*?**

La recursividad sucede cuando una función se llama a sí misma. La iteración ocurre cuando el mismo procesamiento se repite varias veces. Dadas estas definiciones, la diferencia entre recursividad e iteración es que en la primera el problema se divide en subproblemas, llegando finalmente a un caso base. En cambio, la iteración utiliza bloques `for` y `while` para repetir un paso hasta que se cumpla una condición. Esto se relaciona con la notación big *O* mediante la evaluación de eficiencia de los algoritmos. Dado que cada enfoque puede realizar las mismas tareas, pero con eficiencias muy distinta. Lo último mencionado lleva a que existan casos en que uno de los dos es más eficiente que el otro para realizar cierta tarea.

**Explicar la diferencia de rendimiento entre *O(1)* y *O(n)***

Una notación *O(1)* representa un caso en que el número de operaciones es independiente del tamaño de la entrada. Por otro lado, un notación *O(n)* crece directamente proporcional al tamaño de las entradas. Dadas estas definiciones, la diferencia entre estos rendimientos es cómo crece el tiempo de ejecución y el uso de recursos en relación a la entrada, teniendo que un algoritmo *O(1)* es mucho más eficiente que uno   
*O(n)*.

**¿Cómo se calcula el orden en un programa que funciona por etapas?**

Para calcular el orden en un programa que funciona por etapas se realiza mediante el análisis de cada etapa por separado, para luego combinarlas y obtener la complejidad total. El procedimiento sería identificar las etapas del programa y posterior a ello calcular la complejidad de cada una. Finalmente, dependiendo si las etapas se ejecutan de manera secuencial o están anidadas, las complejidades se suman o multiplican, respectivamente.

**¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?**

Determinar la complejidad temporal de un algoritmo recursivo se hace analizando el caso base, las llamadas recursivas y el trabajo que se realiza en cada llamada.

# Obtención de Resultados

Este proyecto calcula la cantidad de caminos posibles entre dos puntos extremos en una grilla, utilizando dos métodos: recursivo y combinatorio. Además, genera un gráfico comparativo de los tiempos de ejecución de ambos métodos para diferentes tamaños de grilla.

## Requisitos

* `Python 3`.
* `Matplotlib`.

## Estructura

1. Cálculo de los caminos entre A y B en una grilla.
2. Generación de gráficos comparativos.

## Parámetros de entrada

El programa está diseñado para trabajar con matrices de tamaños predefinidos. Los tamaños de las grillas que se evalúan son las siguientes

~~~
sizes = [(3,3), (9,9), (12,12), (13,13), (14,14)]
~~~

Es posible modificar estos valores dentro del código si se desea evaluar otroa tamaños de grilla. El formato es `(filas,columnas)`.

## Visualización

El gráfico obtenido compara los tiempos de ejecución de los dos métodos para cada tamaño de grilla. El gráfico incluye:

* **Eje X:** Representa los diferentes tamaños de grilla.
* **Eje Y:** Muestra el tiempo de ejecución en segundos.
* **Líneas**: Una roja que representa el método recursivo y una azul para el método combinatorio.

Este gráfico se guarda como archivo SVG.
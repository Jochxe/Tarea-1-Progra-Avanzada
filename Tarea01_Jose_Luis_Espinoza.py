# Se importan los módulos necesarios
import time
import math
import matplotlib.pyplot as plt

# Decorador que almacena el tiempo de ejecución de una función
def Execution_Time_Deco(func):
    def calculo(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        tf = time.time()
        print(f"Tiempo de ejecución: {tf - t0:.6f} segundos.")
        return result
    return calculo

# Clase que calcula la cantidad posible de caminos entre A y B
class PCB_Paths:
    
    # Se iniciliza el constructor
    def __init__(self, N, M):
        self.N = N # Número de filas
        self.M = M # Número de columnas

    # Método 1: Recursión
    def Recursive_Paths(self, i=1, j=1):

        # Caso Base: Se llega al punto B
        if i == self.N and j == self.M:
            return 1
        
        # Casos Recursivos:
        paths = 0

        if i < self.N: # Todavía puedo bajar
            paths += self.Recursive_Paths(i+1, j) # Me muevo hacia abajo

        if j < self.M: # Todavía puedo avanzar hacia la derecha
            paths += self.Recursive_Paths(i, j+1) # Avanzo hacia la derecha
            
        return paths
    

    # Método 2: Combinatoria
    def Combinatorial_Paths(self):
        # Total de movimientos: (N-1) hacia abajo y (M-1) hacia la derecha
        # El número total de caminos es elegir (N-1) movimientos hacia abajo
        # de un total de (N-1 + M-1) movimientos en total.
        paths = math.comb(self.N + self.M - 2, self.N - 1)
        return paths
    
    # Tiempo de ejecución para el Método 1 (Recursión)
    def Recursive_Time(self):
        t0 = time.time()
        self.Recursive_Paths()
        tf = time.time()
        return tf - t0

    # Tiempo de ejecución para el Método 2 (Combinatoria)
    def Combinatorial_Time(self):
        t0 = time.time()
        self.Combinatorial_Paths()
        tf = time.time()
        return tf - t0

    # Tiempo de ejecución para ambos métodos
    def Execution_Time(self, func, *args, **kwargs):
        t0 = time.time()
        func(*args, **kwargs)
        tf = time.time()
        return tf - t0
    
    # Método que cambia la forma de calcular la respuesta, con decorador
    @Execution_Time_Deco
    def Calculate_Paths(self, method="comb"):
        
        # Se utiliza el método recursivo
        if method == "rec":
            return self.Recursive_Paths()
        
        # Se utiliza el método combinatorio
        elif method == "comb":
            return self.Combinatorial_Paths()
        
        else:
            raise ValueError("Método no soportado. Usar 'rec' o 'comb'.")
        

# ~~~ GENERACIÓN DE GRÁFICOS ~~~

sizes = [(3,3), (9,9), (12,12), (13,13), (14,14)] # Tamaños de matrices a evaluar
recursive_times = [] # Tiempos de ejecución para el Método 1 (Recursivo)
combinatorial_times = [] # Tiempos de ejecución para el Método 2 (Combinatorio)

for N, M in sizes:
    # Se crea una instancia
    pcb_paths = PCB_Paths(N, M)

    # Se obtienen los tiempos de ejecución
    recursive_time = pcb_paths.Recursive_Time()
    recursive_times.append(recursive_time)

    combinatorial_time = pcb_paths.Combinatorial_Time()
    combinatorial_times.append(combinatorial_time)

# Etiquetas para el eje X
sizes_tags = [f"{N}x{M}" for N, M in sizes]

plt.figure(figsize=(10,6))
plt.plot(sizes_tags, recursive_times, label='Recursivo', marker='o', color='r')
plt.plot(sizes_tags, combinatorial_times, label='Combinatorio', marker='s', color='b')

plt.title('Comparación de Tiempos de Ejecución para Diferentes Tamaños de Grilla')
plt.xlabel('Tamaño de la grilla (N x M)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)

plt.savefig('Time_Comparison.svg')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

class Ej8:
    def __init__(self, Tamb, k1, k2, k12, k21):
        # Guardamos los parámetros como atributos de la clase
        self.Tamb = Tamb
        self.k1 = k1
        self.k2 = k2
        self.k12 = k12
        self.k21 = k21

    def derivadas_termicas(self, T1, T2):
        """
        Calcula la tasa de cambio de las temperaturas T1 y T2.
        """
        dT1_dt = -self.k1 * (T1 - self.Tamb) + self.k12 * (T2 - T1)
        dT2_dt = -self.k2 * (T2 - self.Tamb) + self.k21 * (T1 - T2)
        return dT1_dt, dT2_dt

    def euler(self, initial_T1, initial_T2, h, max_simtime):
        """
        Aplica el método de Euler y grafica el resultado.
        """
        # Preparar arreglos de tiempo y variables de estado
        tiempos = np.arange(0, max_simtime + h, h)
        historial_T1 = np.zeros(len(tiempos))
        historial_T2 = np.zeros(len(tiempos))
        
        # Condiciones iniciales
        T1 = initial_T1
        T2 = initial_T2
        historial_T1[0] = T1
        historial_T2[0] = T2

        # Bucle principal de simulación
        for i in range(1, len(tiempos)):
            # 1. Calcular derivadas con el estado actual
            dT1_dt, dT2_dt = self.derivadas_termicas(T1, T2)
            
            # 2. Aplicar paso de Euler: x_{k+1} = x_k + h * f(x_k, t_k)
            T1 = T1 + h * dT1_dt
            T2 = T2 + h * dT2_dt
            
            # 3. Guardar en el historial
            historial_T1[i] = T1
            historial_T2[i] = T2

        self._graficar_resultados(tiempos, historial_T1, historial_T2, "Método de Euler")

    def _graficar_resultados(self, tiempos, T1, T2, titulo):
        """
        Método interno para no repetir el código de ploteo en cada método numérico.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(tiempos, T1, label='T1(t) - Cuerpo 1', color='blue')
        plt.plot(tiempos, T2, label='T2(t) - Cuerpo 2', color='orange')
        plt.axhline(y=self.Tamb, color='red', linestyle='--', label=f'Tamb ({self.Tamb}°C)')
        
        plt.title(f'Evolución Térmica de Dos Cuerpos ({titulo})')
        plt.xlabel('Tiempo (h)')
        plt.ylabel('Temperatura (°C)')
        plt.legend()
        plt.grid(True)
        plt.show()
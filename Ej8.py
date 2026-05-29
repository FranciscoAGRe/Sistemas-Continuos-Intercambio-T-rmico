import numpy as np
import subprocess
import os

class Ej8:
    def __init__(self, Tamb, k1, k2, k12, k21):
        # Guardamos los parámetros como atributos de la clase
        self.Tamb = Tamb
        self.k1 = k1
        self.k2 = k2
        self.k12 = k12
        self.k21 = k21

    def derivadas_termicas(self, T1, T2):
        """Calcula la tasa de cambio de las temperaturas T1 y T2."""
        dT1_dt = -self.k1 * (T1 - self.Tamb) + self.k12 * (T2 - T1)
        dT2_dt = -self.k2 * (T2 - self.Tamb) + self.k21 * (T1 - T2)
        return dT1_dt, dT2_dt

    def euler(self, initial_T1, initial_T2, h, max_simtime):
        """Aplica el método de Euler y grafica el resultado."""
        tiempos = np.arange(0, max_simtime + h, h)
        historial_T1 = np.zeros(len(tiempos))
        historial_T2 = np.zeros(len(tiempos))
        
        T1 = initial_T1
        T2 = initial_T2
        historial_T1[0] = T1
        historial_T2[0] = T2

        for i in range(1, len(tiempos)):
            dT1_dt, dT2_dt = self.derivadas_termicas(T1, T2)
            T1 = T1 + h * dT1_dt
            T2 = T2 + h * dT2_dt
            historial_T1[i] = T1
            historial_T2[i] = T2

        self._graficar_resultados(tiempos, historial_T1, historial_T2, "Método de Euler")

    def _graficar_resultados(self, tiempos, T1, T2, titulo):
        """
        Método interno para graficar utilizando Gnuplot en lugar de Matplotlib.
        """
        # 1. Guardar los arreglos en un archivo de texto plano (.dat)
        data_filename = 'datos_simulacion.dat'
        with open(data_filename, 'w') as f:
            for t, t1, t2 in zip(tiempos, T1, T2):
                f.write(f"{t} {t1} {t2}\n")
        
        # 2. Crear el script con las instrucciones para Gnuplot (.gp)
        script_filename = 'plot_script.gp'
        gnuplot_commands = f"""
        set title 'Evolucion Termica de Dos Cuerpos ({titulo})'
        set xlabel 'Tiempo (h)'
        set ylabel 'Temperatura (°C)'
        set grid
        
        # Definir la temperatura ambiente para la línea constante
        Tamb = {self.Tamb}
        
        # Graficar los datos y la línea de Tamb
        plot '{data_filename}' using 1:2 with lines title 'T1(t) - Cuerpo 1' linecolor rgb 'blue', \\
             '{data_filename}' using 1:3 with lines title 'T2(t) - Cuerpo 2' linecolor rgb 'orange', \\
             Tamb title sprintf("Tamb (%.1f°C)", Tamb) with lines dashtype 2 linecolor rgb 'red'
        """
        
        with open(script_filename, 'w') as f:
            f.write(gnuplot_commands)
            
        # 3. Ejecutar Gnuplot
        try:
            # -persist es equivalente a plt.show(), mantiene la ventana abierta
            subprocess.run(['gnuplot', '-persist', script_filename], check=True)
        except FileNotFoundError:
            print("Error: Gnuplot no está instalado en tu sistema o no se encuentra en el PATH.")
            
        # (Opcional) Descomenta estas líneas si quieres que Python borre 
        # los archivos temporales de Gnuplot luego de graficar:
        # os.remove(data_filename)
        # os.remove(script_filename)
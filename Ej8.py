import numpy as np

class Ej8:
    def __init__(self, Tamb, k1, k2, k12, k21):
        """
        Pre: 
            Tamb, k1, k2, k12, y k21 deben ser valores numéricos (int o float).
        Post: 
            Inicializa la instancia de la clase con las constantes térmicas y de ambiente proporcionadas.
        """
        self.Tamb = Tamb
        self.k1 = k1
        self.k2 = k2
        self.k12 = k12
        self.k21 = k21

    def derivadas_termicas(self, T1, T2):
        """
        Pre: 
            T1 y T2 deben ser valores numéricos que representen las temperaturas en el instante actual.
        Post:
            Devuelve una tupla de dos valores numéricos (dT1_dt, dT2_dt) que representan la tasa de cambio térmico.
        """
        dT1_dt = -self.k1 * (T1 - self.Tamb) + self.k12 * (T2 - T1)
        dT2_dt = -self.k2 * (T2 - self.Tamb) + self.k21 * (T1 - T2)
        return dT1_dt, dT2_dt

    def euler(self, initial_T1, initial_T2, h, max_simtime):
        """
        Pre: 
            initial_T1 y initial_T2 deben ser valores numéricos. h y max_simtime deben ser valores numéricos mayores a 0.
        Post: 
            Devuelve una tupla de tres arreglos numpy (tiempos, historial_T1, historial_T2) 
            de igual longitud con la evolución temporal del sistema calculada mediante el método de Euler.
        """
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

        # Ahora simplemente devolvemos la información en lugar de graficarla aquí
        return tiempos, historial_T1, historial_T2
    
    def heun(self, initial_T1, initial_T2, h, max_simtime):
        """
        Pre: 
            initial_T1 y initial_T2 deben ser valores numéricos. 
            h y max_simtime deben ser valores numéricos mayores a 0.
        Post: 
            Devuelve una tupla de tres arreglos numpy (tiempos, historial_T1, historial_T2)
            de igual longitud con la evolución temporal del sistema calculada mediante el método de Heun.
        """
        tiempos = np.arange(0, max_simtime + h, h)
        historial_T1 = np.zeros(len(tiempos))
        historial_T2 = np.zeros(len(tiempos))

        T1 = initial_T1
        T2 = initial_T2
        historial_T1[0] = T1
        historial_T2[0] = T2

        for i in range(1, len(tiempos)):
            # Calculamos la pendiente actual y predecimos el estado futuro
            dT1_dt, dT2_dt = self.derivadas_termicas(T1, T2)
            T1_pred = T1 + h * dT1_dt
            T2_pred = T2 + h * dT2_dt
            
            # Evaluamos las pendientes en ese estado futuro predicho
            dT1_dt_pred, dT2_dt_pred = self.derivadas_termicas(T1_pred, T2_pred)
            
            # Avanzamos usando el promedio de la pendiente actual y la futura
            T1 = T1 + (h / 2) * (dT1_dt + dT1_dt_pred)
            T2 = T2 + (h / 2) * (dT2_dt + dT2_dt_pred)
            
            # Guardamos el resultado corregido en el historial
            historial_T1[i] = T1
            historial_T2[i] = T2

        return tiempos, historial_T1, historial_T2
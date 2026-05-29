from Ej8 import Ej8
from graficador import exportar_y_graficar

def read_params(filename="parametros.txt"):
    parametros = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or '=' not in line:
                continue
            
            clave, valor = line.split('=')
            clave = clave.strip()
            valor = valor.strip()
            
            try:
                parametros[clave] = float(valor)
            except ValueError:
                print(f"Advertencia: No se pudo convertir '{valor}' a número.")
                
    return parametros

if __name__ == "__main__":
    # Leer parámetros
    params = read_params()

    max_simtime = params['max_simtime']
    h = params['h']
    
    # Inicializar el simulador
    simulador = Ej8(
        Tamb=params['Tamb'],
        k1=params['k1'],
        k2=params['k2'],
        k12=params['k12'],
        k21=params['k21']
    )

    
    tiempos_res, T1_res, T2_res = simulador.euler(
        initial_T1=params['initial_T1'],
        initial_T2=params['initial_T2'],
        h=h,
        max_simtime=max_simtime
    )
    
    # Enviar los datos al script graficador
    exportar_y_graficar(tiempos_res, T1_res, T2_res, params['Tamb'], titulo="Euler")
from Ej8 import Ej8

def read_params(filename="parametros.txt"):
    """
    Lee un archivo de texto y devuelve un diccionario con los parámetros.
    """
    parametros = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or '=' not in line:  # Ignorar líneas vacías o mal formateadas
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
    # 1. Leer parámetros
    params = read_params()

    # 2. Extraer variables de simulación
    max_simtime = params['max_simtime']
    h = params['h']
    
    # 3. Inicializar el simulador con los parámetros del modelo
    simulador = Ej8(
        Tamb=params['Tamb'],
        k1=params['k1'],
        k2=params['k2'],
        k12=params['k12'],
        k21=params['k21']
    )

    # 4. Ejecutar los métodos numéricos
    print("Ejecutando simulación con método de Euler...")
    simulador.euler(
        initial_T1=params['initial_T1'],
        initial_T2=params['initial_T2'],
        h=h,
        max_simtime=max_simtime
    )
    
    # En el futuro, puedes agregar:
    # simulador.rk4(params['initial_T1'], params['initial_T2'], h, max_simtime)
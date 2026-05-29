import subprocess

def exportar_y_graficar(tiempos, T1, T2, Tamb, titulo):
    """
    Guarda los datos generados por la simulación y lanza Gnuplot.
    """

    data_filename = 'datos_simulacion.dat'
    with open(data_filename, 'w') as f:
        for t, t1, t2 in zip(tiempos, T1, T2):
            f.write(f"{t} {t1} {t2}\n")
    
    script_filename = 'plot_script.gp'
    
    gnuplot_commands = f"""
    set title 'Evolucion Termica de Dos Cuerpos ({titulo})' font ',14'
    set xlabel 'Tiempo (h)' font ',12'
    set ylabel 'Temperatura (C)' font ',12'
    
    set key box opaque font ',10' spacing 1.5
    
    set style line 100 lt 1 lc rgb '#e0e0e0' lw 1.0
    set grid ls 100
    
    set style line 1 lt 1 lc rgb '#0072bd' lw 1.5
    set style line 2 lt 1 lc rgb '#d95319' lw 1.5
    set style line 3 lt 2 lc rgb '#d90000' lw 1.5
    
    set offsets graph 0, 0, 0.05, 0.05
    
    Tamb = {Tamb}
    
    plot '{data_filename}' using 1:2 with lines ls 1 title 'T1(t) - Cuerpo 1', \\
         '{data_filename}' using 1:3 with lines ls 2 title 'T2(t) - Cuerpo 2', \\
         Tamb title sprintf("Tamb (%.1f C)", Tamb) with lines ls 3
    """
    
    with open(script_filename, 'w') as f:
        f.write(gnuplot_commands)
        
    # 3. Ejecutar Gnuplot
    try:
        subprocess.run(['gnuplot', '-persist', script_filename], check=True)
    except FileNotFoundError:
        print("Error: Gnuplot no está instalado en tu sistema o no se encuentra en el PATH.")
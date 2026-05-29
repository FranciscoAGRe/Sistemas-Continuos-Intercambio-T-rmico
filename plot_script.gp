
    set title 'Evolucion Termica de Dos Cuerpos (Euler)' font ',14'
    set xlabel 'Tiempo (h)' font ',12'
    set ylabel 'Temperatura (C)' font ',12'
    
    set key box opaque font ',10' spacing 1.5
    
    set style line 100 lt 1 lc rgb '#e0e0e0' lw 1.0
    set grid ls 100
    
    set style line 1 lt 1 lc rgb '#0072bd' lw 1.5
    set style line 2 lt 1 lc rgb '#d95319' lw 1.5
    set style line 3 lt 2 lc rgb '#d90000' lw 1.5
    
    set offsets graph 0, 0, 0.05, 0.05
    
    Tamb = 20.0
    
    plot 'datos_simulacion.dat' using 1:2 with lines ls 1 title 'T1(t) - Cuerpo 1', \
         'datos_simulacion.dat' using 1:3 with lines ls 2 title 'T2(t) - Cuerpo 2', \
         Tamb title sprintf("Tamb (%.1f C)", Tamb) with lines ls 3
    
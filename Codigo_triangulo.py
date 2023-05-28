def calcular_coeficientes_binomiales(n):
    # Crear una lista para almacenar las filas del Triángulo de Tartaglia
    triangulo = []
    
    # Generar las filas del Triángulo de Tartaglia
    for i in range(n+1):
        fila = []
        for j in range(i+1):
            if j == 0 or j == i:
                fila.append(1)
            else:
                coeficiente = triangulo[i-1][j-1] + triangulo[i-1][j]
                fila.append(coeficiente)
        triangulo.append(fila)
    
    # Mostrar los coeficientes binomiales
    for i in range(n+1):
        for j in range(i+1):
            print(triangulo[i][j], end=" ")
        print()
calcular_coeficientes_binomiales(5)
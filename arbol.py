altura = int(input("Ingresa la altura del árbol: "))

# Imprimir la parte superior del árbol
for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

# Imprimir el tronco del árbol
tronco_altura = altura // 2
tronco_ancho = altura // 4

for i in range(tronco_altura):
    espacios_tronco = " " * (altura - tronco_ancho)
    asteriscos_tronco = "*" * tronco_ancho
    print(espacios_tronco + asteriscos_tronco)


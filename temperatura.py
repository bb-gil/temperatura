# Ejercicio NO.2 programa para convertir una cantidad grados C a su equivalente a K y F

# imput

C = input("digite la cantidad de grados C a convertir: ")
C = int(C)

# processing 

F = (C * (9/5)) + 32
K = C + 273.15

# output

print ("Grados Fahrenheit: " + str(F))
print ("Grados Kelvin: " + str(K))

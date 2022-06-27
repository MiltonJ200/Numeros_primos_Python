n1 = int(input("Ingresar el primer numero: "))
n2 = int(input("Ingresar el segundo numero: "))
while (n1<=0 or n2<=0) or n2 <= n1:
    print("Error")
    n1 = int(input("Ingrese primer numero: "))
    n1 = int(input("Ingrese segundo numero: "))

for numero in range(n1, n2+1):
    cantidad_divisor = 0
    for divisor in range(1, numero+1):
        if numero%divisor == 0:
            cantidad_divisor += 1
    if cantidad_divisor == 2:
        print(f"{numero}, es un numero primo ")
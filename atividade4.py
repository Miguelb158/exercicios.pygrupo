# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 


Celsius = float(input("digite a tenperatura que você se encontra:"))
numero = 3
while (numero != 2 and numero != 1):
    numero = int(input(f"voce quer converter essa demperatura de {Celsius}° para?  \n digite 1 para Fahrenheit. \n digite 2 para Kelvin:\n"))
    if (numero == 1 ):
        Fahrenheit = Celsius * 1.8 + 32
        print(f"A tenperatura de {Celsius}° em graus celsius em Fahrenheit é de: {Fahrenheit}.")
    elif (numero == 2):
        Kelvin = Celsius + 273.15 
        print(f"A tenperatura de {Celsius}° em graus celsius em Kelvin é de: {Kelvin}.")
    else:
        print(f"A opeção de numero: {numero} não é valida tente de novo.")
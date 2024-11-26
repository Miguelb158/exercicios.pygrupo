# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 

def calcular_poupanca(gasto_diario):
   
    return gasto_diario * 365

gasto_diario = float(input("Digite o quanto você economiza por dia: R$ "))
poupanca_anual = calcular_poupanca(gasto_diario)
print(f"Você economizará R$ {poupanca_anual:.2f} em 1 ano!")

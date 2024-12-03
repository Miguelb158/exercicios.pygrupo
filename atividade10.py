# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 
import matplotlib.pyplot as plt
import numpy as np
def temp_ordem (dia1, dia2, dia3, dia4, dia5, dia6, dia7 ):
    lista = {dia1, dia2, dia3, dia4, dia5, dia6, dia7}
    numerosordenados = sorted(lista)

    # Dados para o gráfico
    categorias = ["segunda", "tersa", "quarta", "quinta", "sesta", "sabado", "domingo"]
    
    
    # Criar o gráfico de colunas
    plt.bar(categorias, numerosordenados, color='skyblue', edgecolor='black')
    
    # Títulos e rótulos
    plt.title("Exemplo de Gráfico de Colunas", fontsize=16)
    plt.xlabel("Categorias", fontsize=12)
    plt.ylabel("numerosordenados", fontsize=12)
    
    # Adicionar valores no topo das colunas
    for i, valor in enumerate(numerosordenados):
        plt.text(i, valor + 1, str(valor), ha='center', fontsize=10)
    
    # Mostrar o gráfico
    return plt.show()
    

print("insira o dia da semana e a tenperatua que teve em cada dia a:")

segunda = float(input("qual foi a tenperatura da segunda:"))
terça = float(input("qual foi a tenperatura da terça:"))
quarta = float(input("qual foi a tenperatura da quarta:"))
quinta = float(input("qual foi a tenperatura da quinta:"))
sesta = float(input("qual foi a tenperatura da sesta:"))
sabado = float(input("qual foi a tenperatura do sabado:"))
domingo = float(input("qual foi a tenperatura do domingo:"))

temp_ordem (segunda, terça, quarta, quinta, sesta, sabado, domingo  )
 


    

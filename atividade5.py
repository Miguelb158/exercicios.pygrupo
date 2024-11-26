# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 

import statistics

def estatisticas_nivel_rio(niveis_mensais):

    media = sum(niveis_mensais) / len(niveis_mensais)
    mediana = statistics.median(niveis_mensais)
    return {"média": media, "mediana": mediana}

dados_mensais = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]

resultado = estatisticas_nivel_rio(dados_mensais)

print(f"Média do nível do rio: {resultado['média']:.2f} metros")
print(f"Mediana do nível do rio: {resultado['mediana']:.2f} metros")

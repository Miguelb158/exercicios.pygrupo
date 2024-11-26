# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 

def maior_temperatura(dados_climaticos):

    cidade_maior_temp = max(dados_climaticos, key=lambda cidade: dados_climaticos[cidade]["temperatura"])
    return cidade_maior_temp

    '''
    lambda cidade: Define uma função anônima que recebe um único parâmetro (cidade).
    '''
    
dados = {
    "Sorocaba": {"temperatura": 30, "umidade": 50, "vento": 30},
    "Piraciacaba": {"temperatura": 25, "umidade": 65, "vento": 10},
    "São José dos Campos": {"temperatura": 20, "umidade": 80, "vento": 20}
}

print(f"A cidade com maior temperatura é: {maior_temperatura(dados)}")

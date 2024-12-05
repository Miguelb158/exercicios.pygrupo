# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 
#Dados de entrada: Lista de eventos de catástrofes com suas intensidades

eventos = [
    {"tipo": "Enchente", "local": "Cidade Cacapava", "intensidade": 6},
    {"tipo": "Furacão", "local": "Cidade Brasília", "intensidade": 8},
    {"tipo": "Tornado", "local": "Cidade Campos do Jordão", "intensidade": 5},
    {"tipo": "Furacão", "local": "Cidade Campinas", "intensidade": 9},
    {"tipo": "Tornado", "local": "Cidade Sergipe", "intensidade": 7},
    {"tipo": "Furacão", "local": "Cidade São Paulo", "intensidade": 10},
]

eventos_intensos = []

for evento in eventos:
    if evento["intensidade"] > 7:
        eventos_intensos.append(evento)

print("Eventos com intensidade maior que 7:")
for evento in eventos_intensos:
    print(f"{evento['tipo']} em {evento['local']} com intensidade {evento['intensidade']}")

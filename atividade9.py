# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 

def classifica_desastre(intensidade):
    if intensidade <= 3:
        return "Baixo impacto"
    elif 4 <= intensidade <= 6:
        return "Médio impacto"
    elif 7 <= intensidade < 10:
        return "Alto impacto"
    else:
        return "Intensidade inválida"

desastres = {
    "Tremor de terra": 4,
    "Tsunami": 9,
    "Deslizamentos": 5,
    "Ciclones": 7,
    "Tempestade": 6,
    "Onda de Calor": 8,
}

print("Classificação de Desastres:")
for desastre, intensidade in desastres.items():
    classificacao = classifica_desastre(intensidade)
    print(f"{desastre}: Intensidade {intensidade} -> {classificacao}")

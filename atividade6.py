# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 

def calcula_media_temperatura(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

cidades_temperaturas = {
    "Cidade Sorocaba": [25, 28, 26, 24, 27],
    "Cidade Cacapava": [30, 32, 31, 29, 33],
    "Cidade Tatui": [20, 22, 19, 21, 23],
    "Cidade Patinho": [15, 17, 16, 18, 14],
    "Cidade São Paulo": [10, 12, 11, 13, 9],
}

print("Médias de temperatura:")
for cidade, temperaturas in cidades_temperaturas.items():
    media = calcula_media_temperatura(temperaturas)
    print(f"{cidade}: {media:.2f}°C")

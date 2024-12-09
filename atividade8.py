# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27
import csv
def somar_elementos (lista):
    somar = 0 
    for numero in lista:
        somar += numero
    return somar

def media(dias, temp):
    if dias == 0:
        return 0
    return temp / dias
            
with open('arquivo.csv', 'r') as file:
    reader = csv.reader(file)


    somar_Janeiro, dias_Janeiro = 0, 0
    somar_fevereiro, dias_fevereiro = 0, 0
    somar_Março, dias_Março = 0, 0
    somar_Abril, dias_Abril = 0, 0
    somar_Maio, dias_Maio = 0, 0
    somar_Junho, dias_Junho = 0, 0
    somar_Julho, dias_Julho = 0, 0
    somar_Agosto, dias_Agosto = 0, 0
    somar_Setembro, dias_Setembro = 0, 0
    somar_Outubro, dias_Outubro = 0, 0
    somar_Novembro, dias_Novembro = 0, 0
    somar_Dezembro, dias_Dezembro = 0, 0








    for n in reader:
        if n[0] == "Janeiro":
            somar_Janeiro += float(n[2])
            dias_Janeiro += 1

            # ========================================

        elif n[0] == "Fevereiro":
            somar_fevereiro += float(n[2])
            dias_fevereiro += 1

            # ========================================

        elif n[0] == "Março":
            somar_Março += float(n[2])
            dias_Março += 1

            # ========================================

        elif n[0] == "Abril":
            somar_Abril += float(n[2])
            dias_Abril += 1

            # ========================================
             
        elif n[0] == "Maio":
            somar_Maio += float(n[2])
            dias_Maio += 1

            # ========================================

        elif n[0] == "Junho":
            somar_Junho += float(n[2])
            dias_Junho += 1

            # ========================================

        elif n[0] == "Julho":
            somar_Julho += float(n[2])
            dias_Julho += 1

            # ========================================

        elif n[0] == "Agosto":
            somar_Agosto += float(n[2])
            dias_Agosto += 1

            # ========================================
             
        elif n[0] == "Setembro":
            somar_Setembro += float(n[2])
            dias_Setembro += 1

            # ========================================

        elif n[0] == "Outubro":
            somar_Outubro += float(n[2])
            dias_Outubro += 1

            # ========================================

        elif n[0] == "Novembro":
            somar_Novembro += float(n[2])
            dias_Novembro += 1

            # ========================================
             
        elif n[0] == "Dezembro":
            somar_Dezembro += float(n[2])
            dias_Dezembro += 1

    media_Janeiro = media(dias_Janeiro,somar_Janeiro)

    media_fevereiro = media(dias_fevereiro,somar_fevereiro)

    media_Março = media(dias_Março,somar_Março)

    media_Abril = media(dias_Abril,somar_Abril)

    media_Maio = media(dias_Maio,somar_Maio)

    media_Junho = media(dias_Junho,somar_Junho)

    media_Julho = media(dias_Julho,somar_Julho)

    media_Agosto = media(dias_Agosto,somar_Agosto)

    media_Setembro = media(dias_Setembro,somar_Setembro)

    media_Outubro = media(dias_Outubro,somar_Outubro)

    media_Novembro = media(dias_Novembro,somar_Novembro)

    media_Dezembro = media(dias_Dezembro,somar_Dezembro)

    print (f"A temperatura media de cada mês durante esse ano é: \n =================================================\n Janeiro: {media_Janeiro} \n fevereiro: {media_fevereiro}\n março: {media_Março}\n Abril: {media_Abril} \n Maio: {media_Maio}\n Junho: {media_Junho} \n Julho: {media_Julho}\n Agosto: {media_Agosto}\n Setembro: {media_Setembro} \n Outubro: {media_Outubro}\n Novembro: {media_Novembro}\n Dezembro: {media_Dezembro} ")


 


    


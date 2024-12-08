# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 
import csv
def somar_elementos (lista):
    somar = 0 
    for numero in lista:
        somar += numero
    return somar

def media (dias, temp):
    media = temp / dias
    return media
            
with open('arquivo.csv', 'r') as file:
    reader = csv.reader(file)


    Janeiro = []
    somar_Janeiro = []
    dias_Janeiro = []
    media_Janeiro = media(dias_Janeiro,somar_Janeiro)

# ===============================================

    fevereiro = []
    somar_fevereiro = []
    dias_fevereiro = []
    media_fevereiro = media(dias_fevereiro,somar_fevereiro)

# ===============================================

    Março = []
    somar_Março = []
    dias_Março = []
    media_Março = media(dias_Março,somar_Março)
    
# ===============================================

    Abril = []
    somar_Abril = []
    dias_Abril  = []
    media_Abril = media(dias_Abril,somar_Abril)

# ===============================================

    Maio = []
    somar_Maio = []
    dias_Maio = []
    media_Maio = media(dias_Maio,somar_Maio)
    
# ===============================================

    Junho = []
    somar_Junho = []
    dias_Junho = []
    media_Junho = media(dias_Junho,somar_Junho)

# ===============================================

    Julho = []
    somar_Julho = []
    dias_Julho = []
    media_Julho = media(dias_Julho,somar_Julho)

# ===============================================

    Agosto = []
    somar_Agosto = []
    dias_Agosto = []
    media_Agosto = media(dias_Agosto,somar_Agosto)
    
# ===============================================

    Setembro = []
    somar_Setembro = []
    dias_Setembro = []
    media_Setembro = media(dias_Setembro,somar_Setembro)

# ===============================================

    Outubro = []
    somar_Outubro = []
    dias_Outubro = []
    media_Outubro = media(dias_Outubro,somar_Outubro)

# ===============================================

    Novembro = []
    somar_Novembro = []
    dias_Novembro = []
    media_Novembro = media(dias_Novembro,somar_Novembro)
    
# ===============================================

    Dezembro = []
    somar_Dezembro = []
    dias_Dezembro = []
    media_Dezembro = media(dias_Dezembro,somar_Dezembro)








    for n in reader:
        if n[0] == "Janeiro":
            Janeiro.append(float(n[2]))
            somar_Janeiro =(somar_elementos(Janeiro))
            dias_Janeiro = len(Janeiro)

            # ========================================

        elif n[0] == "fevereiro":
            fevereiro.append(float(n[2]))
            somar_fevereiro =(somar_elementos(fevereiro))
            dias_fevereiro = len(fevereiro)

             # ========================================

        elif n[0] == "Março":
            Março.append(float(n[2]))
            somar_Março =(somar_elementos(Março))
            dias_Março = len(Março)

             # ========================================

        elif n[0] == "Abril":
            Abril.append(float(n[2]))
            somar_Abril =(somar_elementos(Abril))
            print (somar_Abril)
            dias_Abril = len(Abril)

             # ========================================
             
        elif n[0] == "Maio":
            Maio.append(float(n[2]))
            somar_Maio =(somar_elementos(Maio))
            print (somar_Maio)
            dias_Maio = len(Maio)

            # ========================================

        elif n[0] == "Junho":
            Junho.append(float(n[2]))
            somar_Junho =(somar_elementos(Junho))
            print (somar_Junho)
            dias_Junho = len(Junho)

             # ========================================

        elif n[0] == "Julho":
            Julho.append(float(n[2]))
            somar_Julho =(somar_elementos(Julho))
            print (somar_Julho)
            dias_Julho = len(Julho)

             # ========================================

        elif n[0] == "Agosto":
            Agosto.append(float(n[2]))
            somar_Agosto =(somar_elementos(Agosto))
            print (somar_Agosto)
            dias_Agosto = len(Agosto)

             # ========================================
             
        elif n[0] == "Setembro":
            Setembro.append(float(n[2]))
            somar_Setembro =(somar_elementos(Setembro))
            print (somar_Setembro)
            dias_Setembro = len(Setembro)

                         # ========================================

        elif n[0] == "Outubro":
            Outubro.append(float(n[2]))
            somar_Outubro =(somar_elementos(Outubro))
            print (somar_Outubro)
            dias_Outubro = len(Outubro)

             # ========================================

        elif n[0] == "Novembro":
            Novembro.append(float(n[2]))
            somar_Novembro =(somar_elementos(Novembro))
            print (somar_Novembro)
            dias_Novembro = len(Novembro)

             # ========================================
             
        elif n[0] == "Dezembro":
            Dezembro.append(float(n[2]))
            somar_Dezembro =(somar_elementos(Dezembro))
            print (somar_Dezembro)
            dias_Dezembro = len(Dezembro)

    print (f"A temperatura media de cada mees durante esse ano é: /n========= /n Janeiro: {media_Janeiro} /n fevereiro: {media_fevereiro}/n Março: {media_Março} Abril: {media_Abril} /n Maio: {media_Maio}/n Junho: {media_Junho} /n Julho: {media_Julho}/n Agosto: {media_Agosto} Setembro: {media_Setembro} /n Outubro: {media_Outubro}/n Novembro: {media_Novembro}/n Dezembro: {media_Dezembro} ")


 


    


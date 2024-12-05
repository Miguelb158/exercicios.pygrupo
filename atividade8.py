# Matheus Villar n° 21 
# Miguel Borges n° 22 
# Pedro Zocatelli n° 27 
import csv
def somar_elementos (lista):
    somar = 0 
    for numero in lista:
        somar += numero
    return somar
            
with open('arquivo.csv', 'r') as file:
    reader = csv.reader(file)


# =========================================================


    Janeiro = []
    somar_Janeiro = []
    Janeiro_dias = []

    for n in reader:
        if n[0] == "Janeiro":
            Janeiro.append(float(n[2]))
            somar_Janeiro =(somar_elementos(Janeiro))
            print (somar_Janeiro)
            Janeiro_dias = len(Janeiro)

    print ("é esse aqui", somar_Janeiro,Janeiro_dias)


 # =========================================================


    fevereiro = []
    somar_fevereiro = []
    Janeiro_dias = []

    for n in fevereiro:
        if n[0] == "Janeiro":
            fevereiro.append(float(n[2]))
            somar_Janeiro =(somar_elementos(fevereiro))
            print (somar_fevereiro)
            dias_fevereiro = len(fevereiro)

    print ("é esse aqui",somar_Janeiro,Janeiro_dias)


    # =========================================================


    marsso = []
    somar_fevereiro = []
    Janeiro_dias = []

    for n in fevereiro:
        if n[0] == "Janeiro":
            fevereiro.append(float(n[2]))
            somar_Janeiro =(somar_elementos(fevereiro))
            print (somar_fevereiro)
            dias_fevereiro = len(fevereiro)

    print ("é esse aqui",somar_Janeiro,Janeiro_dias)


    


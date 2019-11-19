#En entrée on rentre les variables

def entree():
    m=int(input())
    p=int(input())
    return m,p

#Ici on fait les calculs

def calc(m,p):
    for x in range(11):
        y = m*x+p
        print(y)
    return y

#Et la on affiche le resultat finale

def sortie(y):
    print(y)
    
m,p=entree()
y=calc(m,p)
sortie(y)

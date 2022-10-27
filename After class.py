# Instrustions d'affectation logiques arithmetiques
a = 5
b = 6
c = 11
d = a + b - c
a = d - a
c = c - a + b
b = c - b + a
print(a)
print(b)
print(c)
print(d)
# Jeux de Casino - Employes avec grades A, B, C, D
# Salaires en fonction des impots par grade
# A=1%, B=3%, C=2%, D=4%
# f(X) = Y
# Pour les femmes appartenant a D et C, pas d'impot a prelever
grade = "A"
salaire = 300000
sex = 'homme'
age = 41
X1 = salaire/100
Y = salaire - X1
# print(Y)
Y = salaire
if(grade == 'A') :
    X1 = (1 * salaire) / 100
    # Y = salaire - X1
    if (sex == 'homme'):
        if(age >= 40):
            if (salaire > 200000):
                Y = salaire - X1
    else:
        Y = salaire - X1

elif (grade =='B') :
    X1 = (3*salaire)/100
    Y = salaire - X1
elif (grade == 'C') :
    X1 = (2*salaire)/100
    if (sex=='homme'):
        if (salaire >=300000):
            Y = salaire - X1
elif (grade == 'D') :
    X1 = (4*salaire)/100
    Y = salaire - X1
else :
    print ('Error grade inconnu!!!!!')
# Embrication / embriquer les conditions pour les Grades
print(Y)

# Si une personne est de grade A, de sexe masculin, agee de 40 ans ou plus et ayant un salaire de moins de 200000F, pas d'impot.


# Structures de donees
# Liste
# Tuples
entier = 12
entier2 =  '12'
nombre_virgule = 12.3
caracteres = 'bonjour en python'
vrai = True
faux = False
#Listes est une chaine de caracteres est un tableau de caractere
jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
#print(jours[2:4])
jours2 = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
#print(jours + jours2)
jours3 = ('lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche')

#print(jours + jours2)
#les tuples sont en () et les listes en []         happend pour ajouter un element dans liste
jours2.append('News')
jours2[2] = 'Mercredi'
#jours3[3] = 'jezdi'

#print(jours + jours2)

# Les boucles ... ensemble d'instruction qui permettent d'optimiser le code. (3 boucles: pour i allant de 1 a n; ... tant que , ... repeter)
# Boucle while ou tant que / repeter
i = 0
while (i< len(jours2)):
#    print(jours2[i])
    i = i + 1



# Homework : Creer un tableau avec if ---boucler avec personnes [['jean', 200000, 43ans, 'homme' 'A'], ['marie', 300000, 25ans, 'femme', 'C']

grade = "A"
salaire = 300000
sex = 'homme'
age = 41
X1 = salaire/100
Y = salaire - X1
# print(Y)
Y = salaire
if(grade == 'A') :
    X1 = (1 * salaire) / 100
    # Y = salaire - X1
    if (sex == 'homme'):
        if(age >= 40):
            if (salaire > 200000):
                Y = salaire - X1
    else:
        Y = salaire - X1

elif (grade =='B') :
    X1 = (3*salaire)/100
    Y = salaire - X1
elif (grade == 'C') :
    X1 = (2*salaire)/100
    if (sex=='homme'):
        if (salaire >=300000):
            Y = salaire - X1
elif (grade == 'D') :
    X1 = (4*salaire)/100
    Y = salaire - X1
else :
    print ('Error grade inconnu!!!!!')
# Embrication / embriquer les conditions pour les Grades
print(Y)



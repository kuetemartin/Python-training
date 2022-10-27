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
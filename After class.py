
entier=12
entier2='12'
nombre_virgule=12.3
caracteres='bonjour python'
vrai=True
faux=False

#print(entier2 + caracteres)

jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
#print(jours[5:6])
jours2 = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
#print(jours + jours2)
jours3 = ('lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche')
#print(jours3)
#print(jours+jours2)
jours2.append('News')
jours2[2]='Mercredi'
jours2[3]='Jezdi'
#print(jours + jours2)

i = 0
while(i < len(jours2)):
    #print(jours2[0:7])
    i = i + 1


salaire = 2000000
personnes = [['jean',200000,43,'homme','A'],
             ['marie',300000,25,'femme','C'],
             ['jack', 300000, 25, 'homme', 'C'],
             ['elene', 300000, 25, 'femme', 'D'],
             ['daniel', 300000, 25, 'homme', 'C'],
             ['marc', 300000, 25, 'femme', 'A'],
             ['donald', 300000, 25, 'femme', 'Z'],
             ['samuel', 300000, 25, 'femme', 'B'],
             ['audrey', 300000, 25, 'homme', 'A'],
             ['martin', 300000, 25, 'femme', 'C'],
             ['loic', 300000, 50, 'homme', 'A'],
             ]
personnes2 = [['daniel', 300000, 25, 'homme', 'C'],
             ['marc', 300000, 25, 'femme', 'A'],
             ['donald', 300000, 25, 'femme', 'Z'],
             ['samuel', 300000, 25, 'femme', 'B'],
             ['audrey', 300000, 25, 'homme', 'A'],
             ['martin', 300000, 25, 'femme', 'C'],
             ['loic', 300000, 50, 'homme', 'A'],
             ]
i = 0
while(i < len(personnes)):
    #print("Calcul du salaire de " + "personnes[i][0] + "....En cours !")
    Y = personnes[i][1]
    if (personnes[i][4]=='A'):
        X1 = (1 * personnes[i][1])/100
        Y = salaire - X1
        if(personnes[i][3] =='homme'):
            if(personnes[i][2] >= 40):
                if(personnes[i][1] > 200000):
                    Y = personnes[i][1] - X1
                    print (Y)
        else:
            Y = personnes[i][1] - X1
    elif (personnes[i][4] == 'B'):
        X1 = (3 * personnes[i][2])/100
        Y = personnes[i][1] - X1
    elif (personnes[i][4] == 'C'):
        X1 = (2 * personnes[i][1])/100
        if (personnes[i][3] == 'homme'):
            Y = personnes[i][1] - X1
    elif (personnes[i][4] == 'D'):
        X1 = (4 * personnes[i][1])/100
        Y = personnes[i][1] - X1

    else:
        print ('Error de grade !!!!!!.... verifier SVP....')
    print ("Le salaire de " + personnes[i][0] + " est de : " + str(Y))
    i = i + 1

print('##################################################')

print(personnes)
def salaires(personnes2):
    i = 0
    while (i < len(personnes)):
        # print("Calcul du salaire de " + "personnes[i][0] + "....En cours !")
        Y = personnes[i][1]
        if (personnes[i][4] == 'A'):
            X1 = (1 * personnes[i][1]) / 100
            Y = salaire - X1
            if (personnes[i][3] == 'homme'):
                if (personnes[i][2] >= 40):
                    if (personnes[i][1] > 200000):
                        Y = personnes[i][1] - X1
                        print (Y)
            else:
                Y = personnes[i][1] - X1
        elif (personnes[i][4] == 'B'):
            X1 = (3 * personnes[i][2]) / 100
            Y = personnes[i][1] - X1
        elif (personnes[i][4] == 'C'):
            X1 = (2 * personnes[i][1]) / 100
            if (personnes[i][3] == 'homme'):
                Y = personnes[i][1] - X1
        elif (personnes[i][4] == 'D'):
            X1 = (4 * personnes[i][1]) / 100
            Y = personnes[i][1] - X1

        else:
            print ('Error de grade !!!!!!.... verifier SVP....')
        print ("Le salaire de " + personnes[i][0] + " est de : " + str(Y))
        i = i + 1

salaires(personnes2)
print('#######################################################')

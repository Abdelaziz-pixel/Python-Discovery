# exo1: vraie ou faux ?
un=""
deux="février"
if len(un)==0:
    print(False)
else:
    print(True)

if len(deux)==0:
    print(False)
else:
    print(True)

# exo2: Calculer mon âge
année_en_cours = int(input("Saisissez l'année actuel ? "))
année_de_naissance = int(input("Saisissez votre année de naissance ? "))
Vous_êtes_agé_de = année_en_cours-année_de_naissance
print("Vous êtes agé de", Vous_êtes_agé_de, "ans")

# exo3: Problème de chaussures
prix1=70
prix2=59
prix3=20
price=(prix1+prix2+prix3)
somme_des_achats=(price*20/100)
print("Hey bonne nouvelle vous payerais seulement", somme_des_achats, "€")

# exo4: une calculatrice Python
Nombre_1=float(input("Quel est votre nombre ? "))
Nombre_2=float(input("Quel est votre deuxiéme nombre a additioner ? "))
Le_résultat_est = Nombre_1 + Nombre_2
print("Le résultat est", Le_résultat_est)

# exo5: travailler avec les propriétés
Prénom=input("Quel est votre prénom ? ")
Nom=input("Quel est votre nom ? ")
Prénom_1 = (Prénom[0] + Prénom[-1]).upper() 
print(Prénom_1)
Nom_1 = (Nom[0] + Nom[-1]).upper() 
print(Nom_1)
print(Prénom_1 + Nom_1)
Age=float(input("Quel est votre age ? "))
Age_1= Age/33
print(Age_1)

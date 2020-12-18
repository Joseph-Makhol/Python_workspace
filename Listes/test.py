#Questionnaire de vetements
#par Joseph Makhol     makjos02@ecolecatholique.ca

print("Parmi les choix si dessous, choisis un que tu aimes")
ma_liste = ['Nike', 'Adidas', 'Puma', 'Gucci']
print(ma_liste)

choix = input()

if choix == ma_liste[0]:
    print("Nice!")

if choix == ma_liste[1]:
    print("Bon!")

if choix == ma_liste[2]:
    print("Wow!")

if choix == ma_liste[3]:
    print ("Excellent!")

print("Combien de fois par semaine portez-vous cette marque?")
liste = [2, 4, 6]
for i in range(2, 4, 6):
    print (liste)
    choix2 = int(input())
    if choix2 == 2:
        print("okay")

    if choix2 == 4:
        print("WOW!")

    if choix2 == 6:
        print("Go shopping:)")        

print("Merci d'avoir participé a ce petit questionnaire.")        
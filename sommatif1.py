#ce programme déterminera l'équipe de soccer que tu as choisi parmi les choix donner, joue bien dans leur ligue respective.
#par: Joseph Makhol               Email: makjos02@ecolecatholique.ca

r = "real madrid"
a = "arsenal"
c = "chelsea"
b = "bayern munchen"

print("Parmi les choix si dessous, choisis un équipe qui vous imteresse a savoir comment ils font dans leur ligue.")
print("Real Madrid, Arsenal, Chelsea, Bayern Munchen")
 
 #dans cette parti, je donne de l'info au user a propo de l'équipe que a choisi 
choix = input().lower()

if choix == r: 
    print("L'équipe que vous avez choisi ne joue pas a leur meilleur maintenant, ils sont 4e dans leur ligue.")

elif choix == a:
    print("Cette équipe en 2003/2004 etait imbattable, ils sont 14e dans leur ligue.")

elif choix == c:
    print("L'équipe choisie s'est renforcée au cours de l'été grâce à tous les joueurs qui sont venus durant l'été.")

elif choix == b:
    print("Cette équipe vien de gagner le UEFA Champions League et sont maintenant sans doute la meilleure équipe du monde.")

else:
    print("Je n'ai pas compris")    


#ici je demand au user si son equipe de soccer preferer est nommer parmi les examples. si oui, le questionaire continue. Si non, cela est terminer
print("Est-ce que votre équipe preferer est parmi ces choix? Si oui, enter le nom de ton équipe. Si non, dite non.")

user_input = input().lower()

if user_input == r:
    print("Excellent! N'arrêtez pas de les soutenir s'ils vont en Europa League cette saison.")

elif user_input == a:
    print("Ne vous inquiétez pas, vous serez les meilleurs un jour... j'espère.")

elif user_input == c:
    print("Bon choix!")

elif user_input == b:
    print("Excellent choix!!!")

else:
    print("Merci d'avoir participé!")




#Le but etait d'interacter avec le user et savoir quelle est sont équipe preferer parmis les choix.
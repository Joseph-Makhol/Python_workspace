#ce programme déterminera l'équipe de soccer que tu as choisi parmi les choix donner, joue bien dans leur ligue respective.
#par: Joseph Makhol               Email: makjos02@ecolecatholique.ca

r = "real madrid"
a = "arsenal"
c = "chelsea"
b = "bayern munchen"
t = "1999"
ron = "2009"
drog = "2004"
lewa = "2014"
non = "non"


print("Parmi les choix si dessous, choisis un équipe qui vous imteresse a savoir comment ils font dans leur ligue.")
print("Real Madrid, Arsenal, Chelsea, Bayern Munchen")
 
 #Dans cette parti, je donne de l'info au user a propos de l'équipe qui a été choisi 
choix = input().lower()

if choix == r: 
    print("L'équipe que vous avez choisi ne joue pas a leur meilleur maintenant, ils sont 4e dans leur ligue.")

elif choix == a:
    print("Cette équipe en 2003/2004 etait imbattable, ils sont 14e dans leur ligue.")

elif choix == c:
    print("L'équipe choisie s'est renforcée au cours de l'été grâce à tous les joueurs qui sont venus. Ils sont 3e dans leur ligue.")

elif choix == b:
    print("Cette équipe vien de gagner le UEFA Champions League et sont maintenant sans doute la meilleure équipe dans leur ligue et même au monde.")

else:
    print("Je n'ai pas compris")    


#Ici je demand au user si son equipe de soccer preferer est nommer parmi les examples. si oui, le questionaire continue. Si non, cela est terminer
print("Est-ce que votre équipe preferer est parmi ces choix? Si oui, enter le nom de ton équipe. Si non, dite non.")

user_input = input().lower()

if user_input == non:
    print("ok, à la prochaine!!")

elif user_input == r:
    print("Excellent! N'arrêtez pas de les soutenir s'ils vont en Europa League cette saison.")
    print("Je vais vous tester maintenant, dans quelle année est-ce que Cristiano Ronaldo a-t-il rejoint Real Madrid?")

    user_input = input().lower()

    if user_input == ron:
         print("Bravo!")
    else:
        print("uh oh... la bonne reponce est 2009")

elif user_input == a:
    print("Ne vous inquiétez pas, vous serez les meilleurs un jour... j'espère.")
    print("Je vais vous tester maintenant, dans quelle année est-ce que Thierry Henry a-t-il rejoint l'Arsenal?")
    
    user_input = input().lower()

    if user_input == t:
        print("goodjob!!!")
    else:
        print("Êtes vous sûr que vous ètes un suporteur??? La réponce est 1999")   


elif user_input == c:
    print("Bon choix!")
    print("Je vais vous tester maintenant, dans quelle année est-ce que Didier Drogba a-t-il rejoint Chelsea?")
    
    user_input = input().lower()

    if user_input == drog:
        print("goodjob!!!")
    else:
        print("Êtes vous sûr que vous ètes un suporteur??? La réponce est 2004")


elif user_input == b:
    print("Excellent choix!!!")
    print("Je vais vous tester maintenant, dans quelle année est-ce que Robert Lewandowski a-t-il rejoint Bayern Munchen?")
    
    user_input = input().lower()

    if user_input == lewa:
        print("Excellent!!!")
    else:
        print("Je ne pense pas... La bonne réponce est 2014")

else:
    print("Uh oh...")

print("Merci d'avoir participer a mon petit quiz!!!")    

#Le but etait d'interacter avec le user et savoir quelle est sont équipe preferer parmis les choix et le tester pour voir s'il est un vrai fan.

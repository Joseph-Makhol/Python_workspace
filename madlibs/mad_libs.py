#--------------- Jeu de mots ------------------

phrases = []
consignes = []

# changer seulement les lignes dans mon_mad_lib ci-dessous
# --> supprimer les phrases.append et consignes.append
# --> ajouter vos propres phrases et consignes
#
# NE CHANGER RIEN D'AUTRE DANS LE PROGRAMME
#
# Si tout le monde fais ça, je vais pouvoir intégrer le
# travail dans un "livre" de mad libs que vous pourrez
# jouer avec votre famille pendant le temps des fêtes
#

def mon_mad_lib():
    """Préparer les phrases à trou""" 

    # le trou dans la phrase est indiqué par les {}
    phrases.append("Une {} tombe sur ma tête.")
    consignes.append("nom commun")
    phrases.append("Je vais chez le {} pour me faire vérifier.")
    consignes.append("professionnel, masculin")
    phrases.append("il m'a dit de prendre des {} pour ma douleur")
    consignes.append("nom commun")
    phrases.append("Dans le matin, j'ai demander a {} de me faire une petit collation.")
    consignes.append("(ma) nom commun feminin")
    phrases.append("Mon père a crier apres moi et il m'a {}.")
    consignes.append("Verbe à l'infinitif")
    phrases.append("Il y a plusieurs {} facon de demander de faire ma collation tous seul.")
    consignes.append("Adjectif")
        phrases.append("mon père n'est pas come d'autre {}.")
    consignes.append("nom commun")
    phrases.append("Il se fache tres {}.")
    consignes.append("Adverbe")
    phrases.append("Mais, je l'{}.")
    consignes.append("verbe")
    phrases.append("Mes {} on rit de moi après quils on vuent le gros bump sur ma tete")
    consignes.append("Nom commun")
    phrases.append(" j'ai {}.")
    consignes.append("Verbe à l'infinitif")
    phrases.append(" Mes parent on senti ma et ils ont m'acheter un {}.")
    consignes.append("Nom commun")
mon_mad_lib()

# Obtenir les réponses de l'utilisateur
mots = []
# on demande un mot pour chaque consigne, utilisant la boucle 'for each'
for c in consignes:
    # ici le print utilise la méthode .format() qui remplace chaque {}
    # dans le texte avec la valeur dans le .format()
    print("Taper un mot qui est un(e) {}".format(c))
    mots.append(input())


# Afficher le résultat
print("Quand tu est prêt(e) pour le résultat, tape Enter")
input() # attend

for i in range(len(phrases)):
    # les trous {} dans les phrases sont remplacés par les mots.
    print(phrases[i].format(mots[i]))

print("\nMerci d'avoir joué!")
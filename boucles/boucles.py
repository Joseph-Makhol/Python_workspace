# Cela est un programme qui utilise des "while" et des "for" pour te demander des questions.
# par Joseph Makhol   makjos02@ecolecatholique.ca

print("parmi les nombres, choisie un que tu aimerais multiplier par 2")
x = 1
while x < 11:
  print(x)
  x += 1

user_input = float(input())
if user_input < 11:
  print(user_input*2)
else:
  print("Erreur, le numéro que vous avez choisi n'était pas nommer par le programme")

print("Choisi un nombre que tu aimerais diviser en 2")

for i in range(11):
  print(i)
choix = float(input())  
if choix < 11:
  print(choix/2)
else:
  print("Erreur, le numéro que vous avez choisi n'était pas nommer par le programme")


while True:
  print("Veux tu continuer?")

  print("Si non, dit non. Si oui, dit oui")
  end = input().lower()
  if end == "non":
    break
  elif end == "oui":  
    print("CALCULE MENTAL: 5+5 est...")
    ansr = int(input())
    if ansr == 10:
      print("YAY!!!")
    else:
      print("so close:(")
    break
  
print("Merci d'avoir jouer!!!")













  
  
 

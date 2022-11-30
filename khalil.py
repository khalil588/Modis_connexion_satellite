
def v(cellule,variable):
  if cellule == 'NCIN':
    if int(variable) == False or len(variable)!=8:
        print(" le cin doit etre un entier et avoir une longueur qui est égale à 8 ")
        return False
    else :
      if variable[0] == '0':
          return True
      elif variable[0]=='1':
          return True
      else :
        print('le cin doit commencer par 0 ou 1')
        return False
  elif cellule == 'AGE':
    if int(variable) == False :
      print("l'age doit etre un entier")
      return False
    else :
      if int(variable) < 18 :
        print("l'age doit etre superieur à 17 ans ")
        return False
      else :
        return True
  elif cellule=='TYPE' :
    if variable.upper() != 'ADMIN' and variable.upper() != 'ENS'and variable != 'ETUD' :
      print(' le type doit etre égale à ens ou admin')
      return False
    else :
      return True
  else :
    if len(variable) == 0 :
      print('merci de remplir le champ')
      return False
    else:
      if variable.isalpha() :
        return True
      else :
        return False


columns = ['NCIN', 'NOM', 'PRENOM', 'AGE', 'TYPE']


def saisir():
  f = open("Esen.txt", "a+")

  n = False
  while n != True:

    ligne = ""
    for cellule in columns:
      verif = False
      while verif == False:
        phrase = 'merci de saisir votre ' + cellule + ' : '
        variable = input(phrase)
        if v(cellule, variable):
          verif = True
      ligne = ligne + variable + ";"
    ligne += '\n'
    print(ligne)
    f.write(ligne)
    test = 'x'
    while test not in ['y', 'n']:
      test = input(' voulez vous ajoutez une autre enseignant [y/n]')
      if test not in ['y', 'n']:
        print('Merci de saisir soit y soit n ')
      if test == 'n':
        n = True

  f.close()


def etude():
  f = open("Esen.txt", 'r+')
  f1 = open("Etud.txt", "a+")
  linesf = f.readlines()
  print(linesf)
  lst = []
  for number, line in enumerate(linesf):
    ligne = str(line)
    if 'etud' in ligne:
      f1.write(line)
    else:
      lst.append(line)
  f1.close()
  f.close()
  with open("Esen.txt", "w+") as f:
    for  line in lst:
      f.write(line)
      print(line)
  f.close()
def statistiques():
  with open("Esen.txt","r+") as f :
    lines = f.readlines()
    quarante = 0
    adm = 0
    for line in lines :
      ligne = str(line)
      lst = ligne.split(";")
      if lst[4].upper() == 'ADMIN':
        adm+=1
        if int(lst[3])<40 :
          quarante+=1
      if adm == 0:
        adm+=1
  print("la pourcentage du staff administratif ayant un age inferieure à 40 = "+str(quarante/adm)+" %")
  f.close()




saisir()
etude()

statistiques()



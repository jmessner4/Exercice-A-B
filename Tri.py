def tri_liste(liste) :
	n = len(liste)
	for i in range(n) :
		a,b = liste[i],liste[i+1] #création de varible pour la boucle
		if a>b :
			liste[i],liste[i+1]=b,a
			liste[i+1]=a+2
	print(liste)
#is this working ?
#c'est le tour de Tri
#?
#modif depuis la branche 2 pour voir ce que ça fait

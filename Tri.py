def tri_liste(liste) :
	n = len(liste)
	for i in range(n) :
		a,b = liste[i],liste[i+1]
		if a>b :
			liste[i],liste[i+1]=b,a
	print(liste)
#is this working ?
#c'est le tour de Tri
#?

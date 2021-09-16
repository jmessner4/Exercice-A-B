def tri_liste(liste) :
	n = len(liste)
	for i in range(n) :
		a,b = liste[i],liste[i+1]
		if a>b :
			liste[i],liste[i+1]=b,a
	print(liste)
<<<<<<< HEAD
#is this working ?
#c'est le tour de Tri
=======
>>>>>>> 3e908689c69b5ffac3e4445f718b2f677bbcbd2b

subfilo = str(input(""))
classe = str(input(""))
alimentacao = str(input(""))

if(subfilo == "vertebrado"):
	if(classe == "ave"):
		if(alimentacao == "carnivoro"):
			print("aguia")
		if(alimentacao == "onivoro"):
			print("pomba")
	if(classe == "mamifero"):
		if(alimentacao == "onivoro"):
			print("homem")
		if(alimentacao == "herbivoro"):
			print("vaca")
elif(subfilo == "invertebrado"):
	if(classe == "inseto"):
		if(alimentacao == "hematofago"):
			print("pulga")
		if(alimentacao == "herbivoro"):
			print("lagarta")
	if(classe == "anelideo"):
		if(alimentacao == "hematofago"):
			print("sanguessuga")
		if(alimentacao == "onivoro"):
			print("minhoca")


line = input().split(" ")
n1, n2, n3, n4 = line

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

average = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

if(average >= 7.0):
	print("Media: %.1f" %average+"\n"+"Aluno aprovado.")
elif(average < 5.0):
        print("Media: %.1f" %average+"\n"+"Aluno reprovado.")
elif(5.0 <= average <= 6.9):
	rec = float(input(""))
	average2 = (average+rec)/2
	if(average >= 5.0):
		print("Media: %.1f" %average+"\n"+"Aluno em exame."+"\n"+"Nota do exame: %.1f" %rec+"\n"+"Aluno aprovado."+"\n"+"Media final: %.1f" %average2)
	else:
		print("Media: %.1f" %average+"\n"+"Aluno em exame."+"\n"+"Nota do exame: %.1f" %rec+"\n"+"Aluno reprovado."+"\n"+"Media final: %.1f" %average2)

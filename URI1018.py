dinheiro = int(input(""))
resultado = str(dinheiro)+"\n"

mod100 = dinheiro%100
if(mod100 == dinheiro):
    resultado += '%d nota(s) de R$ 100,00\n' %0
else:
    resultado += '%d nota(s) de R$ 100,00\n' %(dinheiro/100)

mod50 = mod100%50
if(mod100 == mod50):
    resultado += "%d nota(s) de R$ 50,00\n" %0
else:
    resultado += "%d nota(s) de R$ 50,00\n" %(mod100/50)

mod20 = mod50%20
if(mod50 == mod20):
    resultado += "%d nota(s) de R$ 20,00\n" %0
else:
    resultado += "%d nota(s) de R$ 20,00\n" %(mod50/20)

mod10 = mod20%10
if(mod20 == mod10):
    resultado += "%d nota(s) de R$ 10,00\n" %0
else:
    resultado += "%d nota(s) de R$ 10,00\n" %(mod20/10)

mod5 = mod10%5
if(mod10 == mod5):
    resultado += "%d nota(s) de R$ 5,00\n" %0
else:
    resultado += "%d nota(s) de R$ 5,00\n" %(mod10/5)

mod2 = mod5%2
if(mod5 == mod2):
    resultado += "%d nota(s) de R$ 2,00\n" %0
else:
    resultado += "%d nota(s) de R$ 2,00\n" %(mod5/2)

mod1 = mod2%1
if(mod1 == mod2):
    resultado += '%d nota(s) de R$ 1,00' % 0
else:
    resultado += '%d nota(s) de R$ 1,00' %mod2

print(resultado)

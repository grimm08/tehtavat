def summa(n):
    x = sum(n)
    print(f"lista {n} summa on {x}")
    return
lista = []
x = input("Anna numero(tyhjä lopettaa) : ")
while x != "":
    x = int(x)
    lista.append(x)
    x = input("Anna numero(tyhjä lopettaa) : ")
if len(lista)>0:
    summa(lista)
else:
    print("lista on tyhjä")




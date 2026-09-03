def new_list(n):
    lista2 = []
    for i in range(len(n)):
        tst = n[i]%2
        if tst == 0:
            lista2.append(n[i])
    return lista2

list = []
num = input("Anna numero (tyhjä lopettaa): ")
while num != "":
    num = int(num)
    list.append(num)
    num = input("Anna numero (tyhjä lopettaa): ")

spin_list = new_list(list)

print(spin_list)

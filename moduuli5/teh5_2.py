lista = []
while True:
    numbs = input("Anna numero: ")
    if numbs == "":
        break
    else:
        lista.append(numbs)

numrs= []
for i in lista:
    i = float (i)
    numrs.append(i)
numrs.sort(reverse=True)
if len(numrs) >5:
    print(numrs[0:5])
else:
    print(numrs)
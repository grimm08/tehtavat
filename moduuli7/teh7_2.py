name_list = set()
names = input("Anna nimi (tyhjä syöte = lopetus): ")
while names != "":
    if names in name_list:
        print ("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        name_list.add(names)
    names = input("Anna nimi (tyhjä syöte = lopetus): ")
for name in name_list:
    print(name)
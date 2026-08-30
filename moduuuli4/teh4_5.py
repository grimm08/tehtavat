adm = "python"
psswrd = "rules"

usr = input("käyttäjätunnus: ").strip(" ")
paswrd = input("salasana: ").strip(" ")
i = 0
if usr == adm and paswrd == psswrd:
    print(f"Trvetuloa")
else:
    while i <5:
        if usr != adm or paswrd != psswrd:
            print("väärä salasana tai käyttäjätuunus")
            i += 1
            usr = input("käyttäjätunnus: ").strip(" ")
            paswrd = input("salasana: ").strip(" ")

    print("Pääsy evätty")
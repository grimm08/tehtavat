while True:
    inchs = float(input("Anna tuuma: "))
    if inchs < 0:
        print("näkämiin")
        break
    else:
        cm = inchs * 2.54
        print(f"{inchs} tuumaa on {cm:.2f} cm")
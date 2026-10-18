l = float(input("Anna leiviskät.\n"))
n = float(input("Anna naulat.\n"))
lud = float(input("Anna luodit.\n"))

ul = l *20 *32
un = n * 32
kaikki = ul + un +lud

all_grams = kaikki * 13.3

Kg = all_grams // 1000
gm = all_grams % 1000

print(f"Massa nykymittojen mukaan:\n"
      f"{Kg:.0f} kilogrammaa ja {gm:.2f} grammaa.")
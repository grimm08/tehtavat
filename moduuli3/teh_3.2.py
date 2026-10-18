from random import choice

print("Valitse hyttiluokka:")
print("LUX on parvekkeellinen hytti yläkannella.")
print("A on ikkunallinen hytti autokannen yläpuolella.")
print("B on ikkunaton hytti autokannen yläpuolella.")
print("C on ikkunaton hytti autokannen alapuolella.")
choice = input("Valitse kirjoittamalla (LUX, A, B tai C):\n").upper()

if choice == "LUX":
    print ("Olet valinnut LUX on parvekkeellinen hytti yläkannella.")

elif choice == "A":
    print ("Olet valinnut A on ikkunallinen hytti autokannen yläpuolella.")

elif choice == "B":
    print("Olet valinnut B on ikkunaton hytti autokannen yläpuolella.")

elif choice == "C":
    print("Olet valinnut C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")
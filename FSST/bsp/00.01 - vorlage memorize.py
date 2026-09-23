import os
import random

# Bildschirm wird gelöscht
os.system('clear')

# Ausgabe der Spiel-Beschreibung
print("In dem Spiel geht es darum, dass du dir die Ziffern-Reihenfolge merkst.")
print("Die neue Ziffer wird dir immer wieder angezeigt.")
print("Du musst dann alle Ziffern in der richtigen Reihenfolge eingeben, durch Bindestriche getrennt.")
print("Trennzeichen ist der Bindestrich. Weiter mit [ENTER]")
input()

all_right = True
values = []
while all_right:
    os.system('clear')
    # Erzeugen des neuen Zufallswertes
    new_number = random.randint(0, 9)
    print(f"Die neue Zahl ist {new_number}. Wie lautet die ganze Folge? (Ziffern durch Bindestriche trennen)")

    # TODO: den neuen Wert in die Liste aller Werte (Variable values) hinzufügen
    values.append(new_number)
    
    text=input()

    # TODO: Umwandeln der Eingabe (z.B. "1-5-9-3") in 
    #       eine Liste von Integer-Werten (z.B. [1, 5, 9, 3]) -->
    #       Ergebnis der Umwandlung in Variable input_values geben 
    nums = text.split("-")
    input_values = []
    for num in nums:
        input_values.append(int(num))

    if len(input_values) != len(values):
        # TODO: Schleifenabbruch über die Variable all_right herbeiführen
        all_right = False
        
        print("Du hast leider nicht mehr alle Zahlen gewusst")

    for i in range(len(input_values)):
        # Überprüfen, ob die einzelnen Werte übereinstimmen
        if values[i] != input_values[i]:
            # Wenn das nicht der Fall ist, dann einen entsprechenden 
            # Hinweis ausgeben und die Schleife beenden
            print(f"Leider ist die Stelle {i} nicht gleich: {input_values[i]} ist nicht {values[i]}")
            all_right = False

# TODO: Ausgabe der Anzahl der richtig gemerkten Werte
count = 0
for i in range(len(input_values)):
    if values[i] == input_values[i]:
        count+=1

print(count)


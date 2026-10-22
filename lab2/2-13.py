# SimpleTriangleTester.py

a = int(input("Inserisci il primo lato: "))
b = int(input("Inserisci il secondo lato: "))
c = int(input("Inserisci il terzo lato: "))

# 1. Ordinamento dei lati in modo che a <= b <= c (tramite scambi)
if a > b:
    temp = a
    a = b
    b = temp

if b > c:
    temp = b
    b = c
    c = temp

if a > b:
    temp = a
    a = b
    b = temp
#altrimenti per ordinare piu facilmente:
#a,b,c = sorted([a,b,c])

# 2. Controllo di esistenza del triangolo (disuguaglianza triangolare: c < a + b)
if a <= 0 or c >= a + b:
    print("non è un triangolo")
elif a == b and b == c:
    # Caso speciale: per l'equilatero non va stampato l'angolo
    print("triangolo equilatero")
else:
    # 3. Classificazione per lati (escluso l'equilatero già gestito)
    if a == b or b == c:
        tipo_lati = "isoscele"
    else:
        tipo_lati = "scaleno"

    # 4. Classificazione per angoli (Teorema di Pitagora sul lato maggiore c)
    diff_quadrati = c * c - a * a - b * b
    if diff_quadrati > 0:
        tipo_angoli = "ottusangolo"
    elif diff_quadrati == 0:
        tipo_angoli = "rettangolo"
    else:
        tipo_angoli = "acutangolo"

    print("triangolo", tipo_lati, tipo_angoli)
# 02-binary8bit.py

n = int(input("Inserisci un numero intero tra 0 e 255: "))

# Estrazione degli 8 bit dal meno significativo (b0) al più significativo (b7)
b0 = n % 2
n = n // 2

b1 = n % 2
n = n // 2

b2 = n % 2
n = n // 2

b3 = n % 2
n = n // 2

b4 = n % 2
n = n // 2

b5 = n % 2
n = n // 2

b6 = n % 2
n = n // 2

b7 = n % 2
n = n // 2

# Stampa dal bit più significativo (b7) al meno significativo (b0)
# sep="" evita gli spazi tra i singoli bit
print("Rappresentazione binaria a 8 bit: ", b7, b6, b5, b4, b3, b2, b1, b0, sep="")
original = 19.99
as_integer = int(original)
back_to_float = float(as_integer)
print("Original:", original)
print("As integer:", as_integer)
print("Back to float:", back_to_float)

#La variabile back_to_float è uguale a original? Perchè? Quali conversioni sono reversibili?
# La variabile back_to_float non è uguale a original perché la conversione da float a int tronca la parte decimale.
# Le conversioni reversibili sono quelle che non perdono informazioni, ad esempio int -> float, 
# float -> int (se il numero è intero), str -> int/float (se la stringa rappresenta un numero).

large_integer = 12345678901234567890 
as_float = float(large_integer) 
back_to_integer = int(as_float) 
print("Original integer:", large_integer) 
print("As float:", as_float) 
print("Back to integer:", back_to_integer) 
print("Difference:", large_integer - back_to_integer)

#Perché c’è una differenza tra large_integer e back_to_integer ?
# C'è una differenza tra large_integer e back_to_integer perché la conversione da float a int tronca la parte decimale, 
# perdendo precisione per numeri molto grandi. In questo caso, la differenza è dovuta alla precisione finita dei numeri in virgola mobile.

result = 0.1 + 0.2 
print(result) 
print(result == 0.3)

#Perché il risultato di 0.1 + 0.2 non è uguale a 0.3?
# Il risultato di 0.1 + 0.2 non è uguale a 0.3 perché la rappresentazione binaria di 0.1 e 0.2 non è esatta, 
# quindi la somma non è esatta. In questo caso, la differenza è dovuta alla precisione finita dei numeri in virgola mobile.


n = 2**53 
n1 = n+1 
n2 = n+2 
print("n:", n) 
print("n1:", n1) 
print("n2:", n2) 
print(n == n1) 
print(n == n2)

nf = float(n)
nf1 = float(n1)
nf2 = float(n2)
print("float(n):", nf) 
print("float(n + 1):", nf1) 
print("float(n + 2):", nf2) 
print(nf == nf1) 
print(nf == nf2)

#Perché n1 e n2 non sono distinti quando convertiti in float?
# Perché la conversione da float a int tronca la parte decimale, perdendo precisione per numeri molto grandi. 
# In questo caso, la differenza è dovuta alla precisione finita dei numeri in virgola mobile.

small = 10 
large = 10**100 
very_large = 10**1000 
print(small) 
print(large) 
print(very_large)

#I numeri vengono rappresentati in modo corretto? Perchè Python riesce a rappresentare correttamente numeri così grandi, ma “sbaglia” con numeri più piccoli come nell’esempio sopra?
#risposta:   i numeri vengono rappresentati in modo corretto perché Python utilizza la rappresentazione in virgola 
# mobile per rappresentare i numeri. 
# Acquisizione dei due orari nel formato 4 cifre (es. 0930)
t1 = int(input("Inserire il primo orario (es. 0930): "))
t2 = int(input("Inserire il secondo orario (successivo al primo): "))

# Estrazione di ore e minuti per il primo orario
ore1 = t1 // 100
min1 = t1 % 100

# Estrazione di ore e minuti per il secondo orario
ore2 = t2 // 100
min2 = t2 % 100

# Conversione in minuti totali trascorsi dalla mezzanotte (00:00)
tot_min1 = ore1 * 60 + min1
tot_min2 = ore2 * 60 + min2

# Minuti in una giornata di 24 ore: 24 * 60 = 1440
# Aggiungendo 1440 e calcolando il resto modulo 1440 si gestisce il passaggio
# per la mezzanotte senza alterare il risultato se t2 >= t1
min_giorno = 24 * 60
diff_min = (tot_min2 - tot_min1 + min_giorno) % min_giorno

# Riconversione della differenza in ore e minuti
ore_trascorse = diff_min // 60
min_trascorsi = diff_min % 60

print("Tempo trascorso:", ore_trascorse, "ore e", min_trascorsi, "minuti")
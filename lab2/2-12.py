# 02-adjective.py

aggettivo = input("Inserisci un aggettivo maschile (-o) o femminile (-a): ")

# Formattazione con solo l'iniziale maiuscola tramite slicing
iniziale = aggettivo[0].upper()
radice = aggettivo[1:-1].lower()
desinenza = aggettivo[-1].lower()

base_formattata = iniziale + radice

if desinenza == "o":
    agg_formattato = base_formattata + "o"
    diminutivo = base_formattata + "ino"
    superlativo = base_formattata + "issimo"
    
    print("Aggettivo inserito:", agg_formattato)
    print("Forma diminutiva:", diminutivo)
    print("Superlativo assoluto:", superlativo)
elif desinenza == "a":
    agg_formattato = base_formattata + "a"
    diminutivo = base_formattata + "ina"
    superlativo = base_formattata + "issima"
    
    print("Aggettivo inserito:", agg_formattato)
    print("Forma diminutiva:", diminutivo)
    print("Superlativo assoluto:", superlativo)
else:
    print("Errore: l'aggettivo non termina con 'o' o con 'a'.")
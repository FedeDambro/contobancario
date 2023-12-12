'''CONTO BANCARIO'''

# Inizializzazione delle variabili
saldo = 0
scelta = 0
sentinella = True


# Richiesta di informazioni all'utente per la creazione dell'account
utente_password = input("Crea una password sicura: ")
utente_nome = input("Inserisci il tuo nome: ")
utente_cognome = input("Inserisci il tuo cognome: ")


# Limiti per le operazioni finanziarie
limite_prelievo = 1000  # Limite massimo per prelievo
limite_versamento = 5000  # Limite massimo per versamento


# Messaggio di benvenuto
print("Benvenuto nella nuova banca, ", utente_nome, utente_cognome)
print("\nScegli una delle seguenti operazioni che vuoi eseguire")


# Loop principale del programma
while scelta != 4:  # Scelta del menù
    print("\nMenù:")
    print('''
        1. Preleva
        2. Versa
        3. Visualizza Saldo
        4. Esci
        \n''')

    
    # Input della scelta dell'utente
    scelta = int(input("Inserisci la tua scelta (1/2/3/4): "))  


    # Operazione di prelievo
    if scelta == 1:
        importo_preleva = float(input("Inserisci l'importo da prelevare: "))
        
        if importo_preleva <= 0:
            print("L'importo del prelievo deve essere maggiore di zero. Operazione annullata.")
            
        elif importo_preleva > saldo or importo_preleva > limite_prelievo:
            print("Operazione annullata. Saldo insufficiente o importo superiore al limite massimo di prelievo.")
            
        else:
            saldo = saldo - importo_preleva
            print("\nHai prelevato: ", importo_preleva, "€. Saldo rimanente: ", saldo, "€.")

    
    # Operazione di versamento
    elif scelta == 2:
        importo_versato = float(input("Inserisci l'importo da depositare: "))
        
        if importo_versato <= 0:
            print("L'importo da versare deve essere maggiore di zero. Operazione annullata.")

        elif importo_versato > limite_versamento:
            print("Operazione annullata. Importo superiore al limite massimo di versamento.")
            
        else:
            saldo = saldo + importo_versato
            print("Hai versato: ", importo_versato, "€.")


    
    # Visualizzazione del saldo
    elif scelta == 3:
        print("\nSaldo attuale: ", saldo, "€.")

    
    # Uscita dal programma
    elif scelta == 4:
        while sentinella:
            
            # Verifica della password per uscire
            tentativo_password_uscita = input("Inserisci la password per uscire: ")
            
            if tentativo_password_uscita == utente_password:
                print("Grazie per aver utilizzato il servizio. Arrivederci!")
                sentinella = False
                
            else:
                print("Password errata per uscire. Riprova.")

  
    # Gestione di una scelta non valida
    else:
        print("\nScelta non valida. Inserire (1/2/3/4). Riprova.")

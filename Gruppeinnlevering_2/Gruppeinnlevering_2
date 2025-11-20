#bakgrunn 
'''
seks uker siden oppstart, står Erling sin gruppe overfor sine 
første utfordringer.
'''

#----------funksjon for riktig inputs---------------

def ask(prompt, valid):
    svar = input(prompt).lower()
    while svar not in valid:
        print("ugyldig valg, prøv igjen")
        svar = input(prompt).lower()
    return svar

#---- Silje og Sivert konflikt 1--------------------
print("Hva bestemmer Erling å gjøre for å løse uenigheten mellom Sivert og Silje?")

Main_choice1 = ask(
    "(møte/bestemme selv): ",
    ('møte', 'bestemme selv')
)

if Main_choice1 == "møte":
    print("Erling velger å ha en møte, hvor Sivert og Silje får sagt meningene sine klart")

    result1 = ask(
        "Etter møtet synes Erling at (begge kom i en kompromiss/begge blir mer løst i sitt mening): ",
        ('begge kom i en kompromiss', 'begge blir mer løst i sitt mening')
    )

    if result1 == "begge kom i en kompromiss":
        print("Erling kan slappe seg at konflikten ble løst mellom Sivert og Silje")
    else:
        print("Erling mislykket til å deskilere konfliken")

else:
    print("Erling gripper inn å bestemme hvordan konflikten skal hånteres")

#------Hamdi og Jabir konflikt 2----------

print("\nBort til Hamdi og Jabir sitt konflikt må Erling ta en valg")

Main_choice2 = ask(
    "(møte/ikke grippe inn): ",
    ('møte', 'ikke grippe inn')
)

if Main_choice2 == "møte":
    print("\nErling velger å ha en møte, hvor Hamdi og Jabir får sagt meningene sine klart")

    result2 = ask(
        "Etter møtet synes Erling at (konflikt løses/begge blir mer løst i sitt mening): ",
        ('konflikt løses', 'begge blir mer løst i sitt mening')
    )

    if result2 == "konflikt løses":
        print("Erling kan slappe seg at konflikten ble løst mellom Hamdi og Jabir")
    else:
        print("Erling mislykket til å håndtere konfliken")

else:
    print("Erling gripper ikke inn og lar konflikten håndteres autonomt")

# -------Motivasjon i teamet--------------------
print("\nErling står i dilemma hvordan han skal håndtere motivasjonen i teamet")

Main_choice3 = ask(
    "Sette tid for relasjonbygging eller prioritere fremdrift (relasjon/fremdrift): ",
    ('relasjon', 'fremdrift')
)

if Main_choice3 == "relasjon":
    print("\nErling velger å bruke aktiviteter og uformelle møter")

    result3 = ask(
        "Ved å bruke tid på relasjonsbygging observerte Erling at medlemmer ble (for avslappet/mer produktiv): ",
        ('for avslappet', 'mer produktiv')
    )

    if result3 == "mer produktiv":
        print("Relasjonbygging fungerte! Teamet skilte sak og person.")
    else:
        print("Medlemmer ble for avslappet. Aktiviteten fungerte ikke pga kort tid.")

else:
    print("Erling prioriterte fremdrift slik at de møtte deadlines og utleverte produktet.")

#---------------------endings--------------------

print("\n ----------------- Sluttresultat -------------------")

# Ending 1
if Main_choice1 == "bestemme selv" and result2 == "konflikt løses" and Main_choice3 == "fremdrift":
    ending = "ENDING 1: Stormen vinner, men et produkt blir utlevert i tide."

# Ending 2
elif (
    Main_choice1 == "møte"
    and result1 == "begge kom i en kompromiss"
    and result2 == "konflikt løses"
    and Main_choice3 == "relasjon"
    and result3 == "mer produktiv"
):
    ending = "ENDING 2: Happy ending! Teamet fungerer godt og portalen lanseres vellykket."

# Default Ending 3
else:
    ending = "ENDING 3: Lansering av portalen mislyktes stort."

print("\n" + ending)


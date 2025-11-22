# Interaktiv historie om Erling og medborgerportalen


#------------------------------------------------------------------------
# Her blir denne funksjonen brukt for å sikre seg at brukeren har skrevet a eller b (store eller små bokstaver)

def valg_input(tekst):
    """Funksjon for å sikre at brukeren skriver A eller B."""
    while True:
        svar = input(tekst).strip().upper()
        if svar in ["A", "B"]:
            return svar
        print("Ugyldig valg – skriv A eller B.\n")


print("\nVelkommen til historien om medborgerportalen!\n")
print("Du spiller som Erling, prosjektleder i et team som står midt i storming-fasen.\n")

# ------------------------------------------------
# BESLUTNING 1 – Konflikten mellom Silje og Sivert

print("KONFLIKT 1: Silje (UX) og Sivert (IT) står i en eskalerende personkonflikt.")
print("A: Du samler teamet til et møte for å rydde opp i misforståelser.")
print("B: Du bestemmer tekniske valg selv for å unngå mer diskusjon.")
valg1 = valg_input("Skriv A eller B: ")

# -------------------------------------------------
# BESLUTNING 2 – Hamdi og Jabir

print("\nKONFLIKT 2: Uenighet mellom Hamdi og Jabir vokser.")
print("A: Du kaller inn til et dialogmøte for å skape forståelse.")
print("B: Du avventer og lar dem håndtere det selv.")
valg2 = valg_input("Skriv A eller B: ")

# ----------------------------------------------------
# BESLUTNING 3 – Motivere teamet

print("\nTEAMET ER PRESSER: Prototypen nærmer seg, og stemningen er anspent.")
print("A: Du prioriterer relasjonsbygging og trygghet i teamet.")
print("B: Du setter alt fokus på fremdrift og leveranser.")
valg3 = valg_input("Skriv A eller B: ")

# -------------------------------
# SLUTTUTFALL

print("\n--- UTFALL ---\n")

# GOD SLUTT – alle tre valg A
if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print("GOOD ENDING – «Fra storm til samarbeid»")
    print("Konfliktene løses gjennom åpen dialog, tilliten styrkes og teamet går inn i norming-fasen.")
    print("Prototypen leveres til tiden med høy kvalitet.")

# DÅRLIG SLUTT – alle tre valg B
elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print("BAD ENDING – «Stormen vant»")
    print("Konfliktene eskalerer, kommunikasjonen bryter sammen og prosjektet blir forsinket.")
    print("Teamet mister motivasjon og relasjoner brytes ned.")

# MIDDELS SLUTT – alt annet
else:
    print("NEUTRAL ENDING – «Kreativt kaos»")
    print("Noen konflikter løses, andre blir ikke fullt løst. Produktet blir levert, men uten felles retning.")
    print("Teamet kommer seg videre, men storming-fasen varer lenger enn nødvendig.")

print("\nTakk for at du spilte!\n")



def sjekksvar(valg): # Håndtere brukerens svar 
   svar = input(valg + " (ja/nei): ").lower()
   if svar == "ja":
        return svar
   elif svar == "nei":
        return svar
   else:
        print("Ugyldig svar, vennligst svar med 'ja' eller 'nei'.")
        


def Konflikt1medsiljeogsivert(): # Konflikt 1
    print("Konflikten mellom Silje og Sivert har eskalert fra sakskonflikt til personkonflikt.")
    svar = sjekksvar("Velger Erling å lage et møte med fokus på kompromiss- og håndteringsmetoden?")
    return svar

def Konflikt2medHamdiogJabir(): # Konflikt 2
    print("Hamdi og Jabir har en uoverenstemmelse som kan forstås som en interessekonflikt/behovkonflikt.")
    svar = sjekksvar("Velger Erling å lage et møte med fokus på aktiv lytting og en tydeligere rollefordeling for å sikre bedre kommunikasjon?")
    return svar

def Konflikthåndtering3medalleifelleskap(): # Konflikt 3
    print("Det er en generell misnøye i teamet som påvirker arbeidsmiljøet.")
    svar = sjekksvar("Velger Erling å arrangere en teambyggingsaktivitet for å styrke samarbeidet og forståelsen blant teammedlemmene?")
    return svar



# Utfall basert på valg ----------------

def utfall1():
    print("Utfall 1 - Stormen vant.")


def utfall2():
    print("Utfall 2 - Fra storm til samarbeid.")

def utfall3():
    print("Utfall 3 - Kommunen lanserer nesten verdens sikreste innloggingsknapp i medborgerportalen.")







# Kode start ----------------
poeng = 0

print("Prosjektleder Erling må finne ut hvordan han kan løse konflikter i teamet sitt.")  # Introduksjon
print("Erling kan velge mellom tre beslutninger for å løse konfliktene")
beslutning1 = Konflikt1medsiljeogsivert()
beslutning2 = Konflikt2medHamdiogJabir()
beslutning3 = Konflikthåndtering3medalleifelleskap()

print(beslutning1 + ", " + beslutning2 + ", " + beslutning3)

if beslutning1 == "ja":
    poeng += 1
if beslutning2 == "ja":
    poeng += 1
if beslutning3 == "ja":
    poeng += 1  


if poeng == 3: # Best utfall
    utfall2()
elif poeng == 2: # Nest best utfall
    utfall1()
else:
    utfall3() # Dårligst utfall
    

    



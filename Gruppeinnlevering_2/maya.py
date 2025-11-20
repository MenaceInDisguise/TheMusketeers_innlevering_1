

print("\nDet oppstår konflikter i gruppen. Erling må ta tak i dem for å sikre et godt samarbeid videre.") # Bruker print for å vise "oppgaven" til brukeren

Konflikt = input("Skriv 1 for Silje og Sivert, 2 for Hamdi og Jabir eller 3 for Noa og Hallgeir: ") # Bruker input for å få brukerens første valg

# Konflikt 1: Silje og Sivert
def Håndter_konflikt_1(): # Bruker def for å lage en funksjon som kan kalles senere
    print("\nDu har valgt å håndtere konflikten mellom Silje og Sivert.") # Bruker print for å vise tekst til brukeren 
    print("\nKonflikt 1:1" "Silje og Sivert har nå en personkonflikt mellom seg.") # Bruker \n for linjeskift og en mer oversiktlig visning
    print("1: Prøv å løse konflikten ved å snakke med dem i plenum.")
    print("2: Ikke involvere seg og la konflikten eskalere.")
    valg = input("Skriv hvilket utfall av konflikten du ønsker (1 eller 2): ")
    if valg == "1": # Bruker if for å sjekke brukerens valg
        print("\nErling bestemmer seg for å snakke med Sivert og Silje i plenum. Konflikten løses i beste fall og teamet kommer videre.")
    elif valg == "2": # Bruker elif for å sjekke et annet valg
        print("\nErling velger å ikke involvere seg, og konflikten mellom Sivert og Silje fortsetter å eskalere. Dette kan føre til forsinkelser i prosjektet.")
    else: # Bruker else for å håndtere ugyldige valg
        print("\nUgyldig valg. Vennligst start på nytt og velg 1 eller 2.")

# Konflikt 2: Hamdi og Jabir
def Håndter_konflikt_2(): # Bruker def for å lage en funksjon som kan kalles senere
    print("\nDu har valgt å håndtere konflikten mellom Hamdi og Jabir.")
    print("\nKonflikt 2: Hamdi og Jabir har en uenighet om hvordan innbyggerne skal kunne delta i digitale folkemøter.")
    print("1: Prøv å løse konflikten ved å kalle inn til et møte.")
    print("2: Ikke involvere seg og la konflikten eskalere.")
    valg = input("Skriv hvilket utfall av konflikten du ønsker (1 eller 2): ")
    if valg == "1":
        print("\nErling bestemmer seg for å kalle inn til et møte med Hamdi og Jabir. Forhåpentligvis fordeles oppgavene rettferdig.")
    elif valg == "2":
        print("\nErling velger å ikke involvere seg, og konflikten mellom Hamdi og Jabir fortsetter å eskalere. Arbeidsfordelingen forblir ujevn.")
    else:
        print("\nUgyldig valg. Vennligst start på nytt og velg 1 eller 2.")

# Konflikt 3: Noa og Hallgeir
def Håndter_konflikt_3(): # Bruker def for å lage en funksjon som kan kalles senere
    print("\nDu har valgt å håndtere konflikten mellom Noa og Hallgeir.")
    print("\nKonflikt 3: Noa og Hallgeir har forskjellige meninger om prosjektets retning.")
    print("1: Prøv å løse konflikten ved å arrangere en workshop.")
    print("2: Ikke involvere seg og la konflikten eskalere.")
    valg = input("Skriv hvilket utfall av konflikten du ønsker (1 eller 2): ")
    if valg == "1":
        print("\nErling bestemmer seg for å arrangere en workshop for Noa og Hallgeir. Dette kan klarlegge retningen og skape enighet.")
    elif valg == "2":
        print("\nErling velger å ikke involvere seg, og konflikten mellom Noa og Hallgeir fortsetter å eskalere. Dette kan føre til uenighet om prosjektets mål.")
    else:
        print("\nUgyldig valg. Vennligst start på nytt og velg 1 eller 2.")


#Håndtering av den andre konflikten uavhengig av hvilken som ble valgt først

if Konflikt == "1":
    Håndter_konflikt_1() # Bruker funksjonen for konflikt 1
    neste = input("\nVil du gå videre til konflikt 2 eller 3? Skriv 2 eller 3 ")
    if neste == "2":
        Håndter_konflikt_2() # Bruker funksjonen for konflikt 2
        print("\nNå gjenstår bare konflikt 3.")
        Håndter_konflikt_3() # Bruker funksjonen for konflikt 3
        print ("Du har nå håndtert alle konfliktene.")

    elif neste == "3": 
        Håndter_konflikt_3()
        print("\nNå gjenstår bare konflikt 2.")
        Håndter_konflikt_2()
        print ("Du har nå håndtert alle konfliktene.")

    else:
        print("\nDette er ikke et alternativ, velg 2 eller 3.")


elif Konflikt == "2":
    Håndter_konflikt_2()
    neste = input("\nVil du gå videre til konflikt 1 eller 3? Skriv 1 eller 3")
    if neste == "1":
        Håndter_konflikt_1()
        print("\nNå gjenstår bare konflikt 3.")
        Håndter_konflikt_3()
        print ("Du har nå håndtert alle konfliktene.")

    elif neste == "3":
        Håndter_konflikt_3()
        print("\nNå gjenstår bare konflikt 1.")
        Håndter_konflikt_1()
        print ("Du har nå håndtert alle konfliktene.")

    else:
       print ("\nDette er ikke et alternativ, velg 1 eller 3.")

elif Konflikt == "3":
    Håndter_konflikt_3()
    neste = input("\nVil du gå videre til konflikt 1 eller 2? Skriv 1 eller 2")
    if neste == "1":
        Håndter_konflikt_1()
        print("\nNå gjenstår bare konflikt 2.")
        Håndter_konflikt_2()
        print ("Du har nå håndtert alle konfliktene.")

    elif neste == "2":
        Håndter_konflikt_2()
        print("\nNå gjenstår bare konflikt 1.")
        Håndter_konflikt_1()
        print ("Du har nå håndtert alle konfliktene.")

    else:
        print("\nDette er ikke et alternativ, velg 1 eller 2.")

else:
    print("\nUgyldig valg. Vennligst start på nytt og velg 1, 2 eller 3.")


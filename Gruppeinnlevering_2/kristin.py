
def mellomrom():
    print()
    print()

#Konflikt 1: mellom Silje og Sivert

def konflikt_1(): # definerer hva som er konflikt 1, og hva som skjer ved valg a eller b
    if Konflikt_1 == "a":
        print("Silje og Sivert kommer frem til et kompromiss og samarbeider bedre fremover.")
    elif Konflikt_1 == "b":
        print("Konflikten mellom Silje og Sivert forverres, og det skaper splid i teamet.")
    else:
        print("Ugyldig valg. Vennligst velg 'a' eller 'b'.")
        
              
  

#Konflikt 2: mellom Hamdi og Jabir

def konflikt_2(): # definerer hva som er konflikt 2, og hva som skjer ved valg a eller b
    if Konflikt_2 == "a":
        print("Erling tar tak i konflikten, og Hamdi og Jabir finner en felles løsning og forbedrer samarbeidet.")
    elif Konflikt_2 == "b":
        print("Erling lar Hamdi og Jabir løse konflikten selv, men de klarer det ikke, og konflikten vedvarer.")
    else:
        print("Ugyldig valg. Vennligst velg 'a' eller 'b'.")
    
        

# Konflikt 3: Relasjonsbygging i teamet


def konflikt_3(): # definerer hva som er konflikt 3, og hva som skjer ved valg a eller b
    if Konflikt_3 == "a":
            print("Erling planlegger sosiale aktiviteter og teamet utvikler sterkere relasjoner og samarbeider bedre på tvers av konflikter.")
    elif Konflikt_3 == "b":
        print("Fokuset på individuelle prestasjoner fører til kortsiktige gevinster, men teamets samarbeid forblir svakt.")
    else:
        print("Ugyldig valg. Vennligst velg 'a' eller 'b'.")        
        
        

#Utfall / slutt

#Utfall 1: Stormen vant

def utfall (konflikt_1, konflikt_2, konflikt_3): # definerer hva som skjer basert på hvilke kombinasjoner av valg a og b som er gjort, og definerer utfallet av prosjektet. 
    if konflikt_1 == "a" and konflikt_2 == "a" and konflikt_3 == "a":
        print("Teamet blir sterkere etter å ha løst konflikter, og samarbeidet forbedres") #utfallet om alle valg er a
    elif konflikt_1 == "b" and konflikt_2 == "b" and konflikt_3 == "b":
        print("Teamet faller fra hverandre, og prosjektet mislykkes på grunn av dårlig samarbeid og konflikter.") #utfallet om alle valg er b
    else:
        print("prosjektet gjenomføres greit, men konfliktene er fortsatt til stede i teamet.") #utfallet om en blanding av valg a og b er gjort
        
        




#--------- kode
print("Prosjektleder Erling skal ta valg for å håndtere konflikter i team") 
print("Skal bruke tre beslutningspunkter for Erling sine hovedvalg")
mellomrom()
Konflikt_1 = input("Det er konflikt mellom Silje og Sivert. Valg a: Vil Erling ta tak i konflikten? Valg b: Vil Erling overse konflikten? (a/b) ")
konflikt_1() 
mellomrom()
Konflikt_2 = input("Det er konflikt mellom Hamdi og Jabir. Valg 1: Vil Erling mekle mellom dem? Valg 2: Vil Erling la dem løse det selv og observere dem først? (a/b) ")
konflikt_2() 
mellomrom()   
Konflikt_3 = input("Det er generelle samarbeidsproblemer i teamet. Valg 1: Vil Erling arrangere sosiale aktiviteter og fokusere på teambygging? Valg 2: Vil Erling fokusere på individuelle prestasjoner, med fremdtift og leveranse? (a/b) ")
konflikt_3()
mellomrom()
print(Konflikt_1 + " " + Konflikt_2 + " " + Konflikt_3)
print("Erling har nå tatt sine valg for å håndtere konfliktene i teamet.")
utfall(Konflikt_1, Konflikt_2, Konflikt_3)
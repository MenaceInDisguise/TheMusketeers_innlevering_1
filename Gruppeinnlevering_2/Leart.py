#------------------------------------------------------------------ Introduksjon og setting ---------------------------------------------------------------------
print("Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal, samlet sitt prosjektteam for første gang.")
print("Etter en inspirerende oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver.\n")
print("Det oppstår en konflikt mellom Silje og Sivert, og Erling forstår at han må ta en avgjørelse før samarbeidet blir verre.")
print("Hva velger Erling å gjøre?")
print("A: Erling samler teamet til et møte hvor Silje og Sivert får muligheten til å uttrykke synspunktene sine og misforståelsene sine.")
print("B: Erling bestemmer scopet til medborgerportalen selv.")

#----------------------------------------------------------------- Første valg: Konflikten mellom Silje og Sivert ----------------------------------------------
valg1 = input("Hva velger Erling? (A/B):")
if valg1 == "A":
    # Brukeren valgte å håndtere konflikten åpent
    print("Du valgte å samle teamet til et møte.")
    print("Silje og Sivert får uttrykt synspunktene sine og ryddet opp i misforståelser, begge blir hørt og dette gjør at de kommer til et felles kompromiss.\n")
    
else:
    # Brukeren valgte å ta beslutningen alene
    print("Du valgte å bestemme scopet selv.")
    print("Dette påvirker resten av prosjektet negativt. Silje og Sivert liker ikke å jobbe med hverandre og konflikten skaper et dårlig arbeidsmiljø som går utover resten av teamet.\n")

print("Samtidig med konflikten mellom Silje og Sivert oppstår det spenning mellom Hamdi og Jabir.")
print("De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter.")
print("A: Erling tar tak i uenigheten før den vokser og innkaller til et felles møte.")
print("B: Erling velger å ikke gripe inn med engang, men heller observere hvordan Hamdi og Jabir håndterer uenigheten på egen hånd.")

#----------------------------------------------------------------- Andre valg: Uenighet mellom Hamdi og Jabir ---------------------------------------------------
valg2 = input("Hva velger Erling? (A/B): ")
if valg2 == "A":
    # Brukeren valgte å ta tak i problemet med en gang
    print("Du valgte å innkalle til et felles møte.")
    print("Møtet skaper forståelse og de finner et kompromiss mellom kontroll og åpenhet i løsningen.\n")
else:
    #Brukeren valgte å ikke gripe inn
    print("Du valgte å ikke gripe inn med engang.")
    print("Konflikten vokser i det skjulte og sprer seg til resten av teamet.\n")
    
print("Etter de tidligere konfliktene i teamet er stemningen spent og prosjektet nærmer seg første prototype-milestone.")
print("Erling må finne en balanse mellom å holde fremdriften og samtidig ivareta teamets motivasjon.")
print("Hva velger Erling å gjøre? (A/B): ")
print("A: Han velger å sette av tid til relasjonsbygging og sosiale aktiviteter, med mål om å styrke tillit, samarbeid og kommunikasjon i gruppen.")
print("B: Erling velger å prioritere fremdrift og leveranser fremfor sosiale aktiviteter.")

#---------------------------------------------------------------- Tredje valg: Teamets motivasjon vs fremdrift --------------------------------------------------
valg3 = input("Hva velger Erling? (A/B): ")
if valg3 == "A":
    # Brukeren prioriterer relasjonsbygging
    print("Du valgte å sette av tid til relasjonsbygging og sosiale aktiviteter.")
    print("Dette fører til at teamet blir mer sammensveiset og forbedrer kommunikasjonen fremover.\n")
else:
    #Brukeren prioriterer leveranse
    print("Du valgte å prioritere fremdrift og leveranser fremfor sosiale aktiviteter.")
    print("Dette holder prosjektet på tidsplan og sikrer at prototypen leveres som planlagt, men svekker motivasjonen og samarbeidet, og konflikter forverres.\n")
    
#--------------------------------------------------------------- Slutt: Bestem utfall basert på kombinasjonen av valg -------------------------------------------
if valg1 == "A" and valg2 == "A" and valg3 == "A":
    # Alle valg fremmer samarbeid - god ending
    print("SLUTT 1: Good ending - Fra storm til samarbeid")
    print("""
    Erling velger å møte utfordringene med åpenhet og empati ved å samle teamet til et møte.
    Silje og Sivert får uttrykke synspunktene sine og rydder opp i misforståelser.
    De finner et felles kompromiss som skaper ro i teamet.
    Erling arrangerer også et dialogmøte mellom Hamdi og Jabir, hvor de blir enige om en trygg og åpen løsning.
    Stemningen i gruppen løftes, og kommunikasjonen blir mer preget av respekt og samarbeid.
    Erling lærer av konfliktene gjennom refleksjon, noe som styrker lederrollen hans.
    Han setter av tid til teambuilding og en felles lunsj som gir økt trygghet og motivasjon.
    Teamet begynner å dele ideer mer fritt, og kvaliteten på arbeidet forbedres.
    
    Prosjektet når milepælen med første prototype til rett tid, og gruppen går inn i norming-fasen.
    """)

elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    # Alle valg unngår konfliktløsning - dårlig ending
    print("SLUTT 2: Bad ending - Stormen vant")
    print("""
    Erling forsøker å balansere fremdrift og forhold i teamet, men etter seks uker har
    de beveget seg nærme storming-fasen preget av uenigheter, maktkamp og usikkerhet om roller.
    Erling forsøker å balansere tid og relasjoner, men mangler evnen til å håndtere konflikter, manglende strategi til å konflikthåndtere internt.
    Sakskonflikten mellom pårørende har blusset opp til personkonflikter, emosjoner og identitet dominerer fremfor sak.
    Uten strukturert dialog mister gruppen trygghet, og relasjonene mellom dem svekkes.
    
    Prototypen presenteres, teknisk er den bra - men ingen feirer.
    Silje melder ifra at hun trekker seg.
    Sivert er stille.
    Jabir og Hamdi er også stille.
    Erling kjenner at prosjektet overlevde, men ikke egentlig levde.
    
    Teamet kom aldri ut av stormen.
    """)

else:
    # Alle andre kombinasjoner - mid ending
    print("SLUTT 3: Mid ending - Kommunen lanserer (nesten) verdens sikreste innlogging-knapp!")
    print("""
    Erling bestemmer seg for å la folk "finne ut av det selv" - et valg som er veldig... modig.
    Silje lager en teknologisk knapp som endrer farge etter humør.
    Sivert låser knappen bak seks brannmurer.
    Jabir lar innbyggerne tegne direkte på skjermen.
    Hamdi er den eneste som tar det seriøst.
    
    Det tar 5 minutter før prototypen kræsjer.
    Teamet kaller det en "interaktiv stesstest" for å unnslippe pinligheten.
    
    Erling sin strategi med lav intervensjon fører til kreativt kaos.
    Prosjektet forsinkes, men gruppen finner et snev av samhold gjennom humør og selvironi.
    """)

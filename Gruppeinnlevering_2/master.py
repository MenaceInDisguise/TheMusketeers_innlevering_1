
def avsnitt(): #for å lage mellomrom i terminalen mellom info
    print()
    print()


def sjekkSvar(spm): # Funksjon for å håndtere bruker input, bruker loop så brukeren må gi et gyldig svar før den går videre
    while True:
        svar = input(spm + " (a/b) ").lower().strip() # fjerner mellomrom og gjør alt til små bokstaver. og henter spørsmålet fra funksjons parameteren
        if svar in ("a", "b"):
            return svar
        else:
            print("Feil input, skriv a eller b")





# -------------------- Historie funksjoner --------------------------------
def introduksjon(): ## introduksjon
    print("Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal, samlet sitt prosjektteam for første gang. Etter en inspirerende oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver.")

#-------------------- Første beslutning -------------------- printer info og kaller på en funksjon som henter brukerinput og returnerer verdien brukeren svarer på spørsmålet slik at vi kan lagre det å bruke det til senere
def beslutningspunkt1():
    print("Beslutning 1:")
    print("Under utviklingen av medborgerportalen blir Silje og Sivert uenige om scopet, silje mener at scopet til medborgerportalen burde være stor slik at brukerne skal ha mer frihet i utvikling og bruk av portalen. Derimot har Sivert lyst til å begrense scopet til prosjektet slik at det blir realistisk og et fornuftig bruk av ressurser.")
    avsnitt()
    svar = sjekkSvar("(a) Erling velger å møte utfordringene med åpenhet og empati ved å samle teamet til et møte.  I dette møtet får Silje og Sivert mulighet til å uttrykke synspunktene sine og misforståelsene sine. (b) Erling bestemmer scopet til medborgerportalen selv, utfallet blir at Sivert og Silje ender opp på dårlig fot med hverandre, uro og stress tar over arbeidsmiljøet.")
    return svar


#-------------------- Andre beslutningspunkt --------------------


def beslutningspunkt2():
    avsnitt()
    print("Beslutning 2:")
    print("Samtidig med konflikten mellom Silje og Sivert oppstår det spenning mellom Hamdi (kulturavdelingen) og Jabir (brukerrepresentant).De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter: Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform. Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill. Foreløpig er uenigheten lavmælt, men Erling merker at frustrasjonen vokser. Prosjektet nærmer seg en viktig milepæl: første prototype skal være klar om tre uker. Stemningen er spent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan avgjøre om teamet beveger seg videre mot “norming” – eller blir stående fast i stormen.")
    avsnitt()
    svar = sjekkSvar("(a) Erling bestemmer seg for å ta tak i den uenigheten mellom Hamdi og Jabir før den vokser. Han innkaller til et felles møte der målet er å skape forståelse og finne et kompromiss mellom kontroll og åpenhet i løsningen. (b) Erling velger å ikke gripe inn med en gang, men heller observere hvordan Hamdi og Jabir håndterer uenigheten på egen hånd.")
    return svar



#-------------------- Tredje beslutningspunkt --------------------

def beslutningspunkt3(): 
    avsnitt()
    print("Beslutning 3:")
    print("Etter de tidligere konfliktene i teamet, er stemningen spent og prosjektet nærmer seg første prototype-milestone. Erling må finne en balanse mellom å holde fremdriften og samtidig ivareta teamets motivasjon.")
    avsnitt()
    svar = sjekkSvar("(a) Erling velger å sette av tid til relasjonsbygging og sosiale aktiviteter, med mål om å styrke tillit, samarbeid og kommunikasjon i gruppen. (b) Erling fokuserer utelukkende på å nå milepælen for prototypen, og legger til side sosiale aktiviteter for å sikre at teamet leverer i tide.")
    return svar

#------------------- Slutt --------------------

def utfall1(): # Stormen vant
    avsnitt()
    print("Utfall: Stormen vant")
    print("Erling forsøker å balansere fremdrift og forhold i teamet, men etter seks uker har de beveget seg nærmere storming-fasen preget av uenigheter, maktkamp og usikkerhet om roller. Erling forsøker å balansere tid og relasjoner, men mangler evnen til å håndtere konflikter, manglende strategi til å konflikthåndtere internt. Sakskonflikten mellom pårørende har blusset opp til personkonflikter; emosjoner og identitet dominerer fremfor sak. Saklige diskusjoner blir ikke opprettholdt (Gjøsund & Huseby, 2023); hvor kommunikasjon er særpreget reaktivitet og tolking i stedet for å lytte hva personen har å si, Frustrasjoner tar over; noe som peker på skjult konflikt som ikke blir tatt tak i (Jacobsen, 2016). Uten strukturert dialog mister gruppen trygghet, og relasjonene mellom dem svekkes. Prototypen presenteres, teknisk er den bra – men ingen feirer. Silje melder ifra at hun trekker seg, Sivert er stille, Jabir og Hamdi er det stille. Erling kjenner at prosjektet overlevde, men ikke egentlig levd. Teamet kom seg aldri ut av stormen.")

def utfall2(): # Good ending - “Fra storm til samarbeid”
    avsnitt()
    print("Utfall: Fra storm til samarbeid")
    print("Erling velger å møte utfordringene med åpenhet og empati ved å samle teamet til et møte. I dette møtet får Silje og Sivert uttrykke synspunktene sine og misforståelsene blir ryddet opp, som gjør at de finner et felles kompromiss. Erling arrangerer også et dialogmøte mellom Hamdi og Jabir hvor de blir enige om en trygg og åpen løsning. Resultatet av møtene hever stemningen i gruppa og fører til åpen kommunikasjon, økt tillit og motivasjon. Teamet utvikler en felles kommunikasjonskultur basert på respekt og åpenhet. Erling lærer av konfliktene gjennom refleksjon, noe som styrker lederrollen hans. Erling setter også av tid til en kort teambuilding aktivitet og en felles lunsj for teamet. Her blir de enda bedre kjent med hverandre og får sjansen til å møtes i en sosial og relasjonsbyggende sammenheng. Den nye tryggheten teamet har etablert gjør at medlemmene tør å komme med nye ideer, som gjør kvaliteten på prosjektet mye bedre. Prosjektet når milepælen med første prototype til rett tid og går inn i norming fasen.")

def utfall3():
    avsnitt()
    print("Utfall: Kommunen lanserer (nesten) verdens sikreste innlogging knapp i medborgerportalen")
    print("Erling bestemmer seg for å la folk “finne ut av det selv” – et valg som er veldig… modig. Silje lager en teknologisk knapp som endrer farge etter humør, som en Taurus, er Silje er veldig emosjonell. Sivert velger å låse knappen bak seks brannmurer, og Jabir mener at fri vilje og frihet er viktig; han gir innbyggerne mulighet til å tegne meningene sine direkte på skjermen. Hamdi er den eneste som tar det seriøst. Det tar 5 minutter før prototypen under presentasjonen kræsjer. De forkledde presentasjonen som “interaktiv stress test” for å unnslippe pinligheten. Prosjektet er forsinket. Erling har brukt en tilnærming hvor teamet “selvregulerer seg” gjennom storming fasen. En lav intervensjon kan virke frigjørende i modne teams, men i denne rollen med usikkerhet og uklare roller fører det til kreativt kaos. Vi ser det blusser opp praktiske løsninger. Innovative? Ja, men ikke særlig effektivt eller etterspurt etter. Kommunikasjonen er enveis hvor alle snakker, men ingen lytter. Prosjektet forsinkes, oppnår gruppen et snev av norming gjennom humor og selvironi.")

#-------------------- Main funksjon ------------------------
poeng = 0 #Lager variabel for å telle poeng basert på om brukeren velger a eller b, a er positive valg dermed blir det et pluss poeng

introduksjon()
avsnitt()
b1 = beslutningspunkt1()
b2 = beslutningspunkt2()
b3 = beslutningspunkt3()

if b1 == "a": # hvis bruker velger a så gir vi et pluss poeng
    poeng += 1
if b2 == "a":
    poeng += 1
if b3 == "a":
    poeng += 1


if poeng == 3: #hvis du har 3 poeng får du det positive utfallet
    utfall2()
elif poeng == 2: #hvis du har 2 poeng får du et mindre positivt utfall
    utfall1()
else: # hvis du har 1 eller mindre poeng så får du det værste utfallet
    utfall3()
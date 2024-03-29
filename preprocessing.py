#in dit python bestand worden de afbeeldingen met veel filters en bewerkingen klaar gemaaakt voor classificatie. het doel is om fotos van enkele cijfers te veranderen in afbeeldingen die erg lijken op de afbeeldingen in de MNIST dataset, waar het model op getraind is.

#eerst moeten de nodige libraries geimporteerd worden:
import cv2 #voor al het werk rondom afbeeldingen aanpassen
import numpy as np #vooral voor numpy arrays, dit is een datatype dat een soort stoere list is, een list heeft 1 dimensie, maar een numpy array kan ook meerdere dimensies hebben, waardoor je matrices en tensoren kan opslaan in variabelen

#functie die de afbeeldingen preprocesst:
def preprocess(afbeelding): #de afbeelding is in het eindpunt al ingelezen met cv2, dat hoeft niet meer
    grijs = cv2.cvtColor(afbeelding, cv2.COLOR_BGR2GRAY) #maakt de afbeelding zwartwit. dit laat de dimensies van de afbeelding van (hoogte, breedte, 3) gaan naar (hoogte, breedte, 1)
    ietskleiner = cv2.resize(grijs, (255, 255)) #maakt de afbeelding van welk formaat dan ook vierkant en 255 pixels groot. hierna zijn de dimensies (255, 255). de dimensie die het aantal kleurkanalen weergeeft is dus weg, deze wordt later terug gebracht.
    denoise = cv2.fastNlMeansDenoising(ietskleiner, 13, 13, 7, 7) #haalt het meeste ruis weg, in gebieden van 13x13. de tweede 13 is het vergelijkingsgebied, en de functie heeft een intensiteit van 7
    binair = cv2.adaptiveThreshold(denoise, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4) #maakt alle lichte pixels helemaal zwart en alle donkere pixels (voornamelijk het cijfer) wit. de maximale waarde is 255 (wit). de omringende 11 pixels worden meegenomen, en 4 is de afwijking (4 werkte voor in dit geval het best, met deze waardes is het vooral veel proberen en kijken wat werkt)
    kernel = np.ones((2, 1), np.uint8) #maakt een 3x2 matrix (numpy array) aan gevuld met alleen maar integer 1en. deze wordt gebruikt als kernel (een soort filter) om de afbeelding in de volgende regel over te gaan.
    lijnweg = cv2.morphologyEx(binair, cv2.MORPH_OPEN, kernel) #deze functie werkt goed tegen horizontale lijnen. hij haalt de buitenste randen van kleurgebieden die de vorm van de kernel hebben (3x2) weg. dit heet erosion. daarna voegt hij weer een rand pixels toe aan de kleurgebieden (dilation). hierdoor blijven grote objecten zoals cijfers er nagenoeg hetzelfde uitzien, maar dunne horizontale dingen, zoals de lijnen die weg moeten, zijn door de erosion helemaal verdwenen en komen door dilation dus ook niet meer terug.
    kernel = np.ones((3, 3), np.uint8) #maakt een nieuwe kernel aan, van 3x3 dit keer.
    thicc = cv2.dilate(lijnweg, kernel, iterations=1) #deze functie maakt overgebleven objecten wat dikker, zodat er meer van overblijft als de ofbeelding straks kleiner gemaakt wordt.
    alle_contouren, _ = cv2.findContours(thicc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #zoekt de contouren van kleurgebieden en slaat deze op in een lijst. de tweede variabele die cv2.findContours oplevert is de volgorde van groottes van de gevonden contouren. deze zijn voor dit doeleinde niet nodig, dus worden ze aan de variabele '_' gegeven.
    gefilterde_contouren = [] #soms zitten er aan de randen van de afbeelding hier nog wat witte objecten die geen cijfer zijn. denk hierbij aan misschien de rand van het blaadje of een stukje van een ander cijfer. De code neemt aan dat objecten die tegen de rand van de afbeelding aanzitten geen cijfer zijn, dus deze moeten eruit gefilterd worden.
    margin = 3 #objecten die binnen 3 pixels van de rand zitten worden niet meegenomen.
    for contour in alle_contouren: #loopt alle contouren 1 voor 1 na
        x, y, breedte, hoogte = cv2.boundingRect(contour) #pakt de x- en y-coordinaten van de linkerbovenhoek van de zo klein mogelijke rechthoek die om de contour getekent kan worden, en de breedte en hoogte van deze rechthoek.
        if x > margin and y > margin and x + breedte < ietskleiner.shape[1] - margin and y + hoogte < ietskleiner.shape[0] - margin: #checkt of de contouren binnen de margin van 3 pixels van de rand of liggen
            gefilterde_contouren.append(contour) #ligt de contour niet dicht bij de rand, wordt hij opgeslagen in de lijst met goede contouren.

    grootste_contour = max(gefilterde_contouren, key=cv2.contourArea) #pakt de contour met de grootste oppervlakte. dit is waarschijnlijk het cijfer.
    x, y, breedte, hoogte = cv2.boundingRect(grootste_contour) #pakt weer de x- en y-coordinaten van de linkerbovenhoek van de rechthoek om de grootste contour, en ook de breedte en hoogte.
    margin = 10 #de afbeelding wordt bijgesneden, en aan elke kant van de rechthoek moeten nog 10 pixels margin zitten.
    x -= margin #berekent de x-coordinaat van de linkerbovenhoek van de rechthoek met margin
    y-= margin #berekent de y-coordinaat van de linkerbovenhoek van de rechthoek met margin
    breedte += 2 * margin #berekent de nieuwe breedte (twee keer de margin omdat aan elke kant de margin bij moet)
    hoogte += 2 * margin #berekent de nieuwe hoogte
    cijfer = thicc[y:y+hoogte, x:x+breedte] #knipt de rechthoek met margin uit de preprocessed afbeelding, om het waarschijnlijke cijfer heen
    max_lengte = max(breedte, hoogte) #pakt of de breedte of de hoogte, welke van de twee het langste is
    vierkantcijfer = cv2.resize(cijfer, (max_lengte, max_lengte)) #vervormt het waarschijnlijke cijfer zodat het vierkant is
    resize = cv2.resize(vierkantcijfer, (28, 28), interpolation=cv2.INTER_NEAREST) #maakt de afbeelding 28x28, zoals het model verwacht. de dimensies van de afbeelding zijn nu dus (28, 28)
    kleurkanaal = np.expand_dims(resize, axis=0) #voegt de derde dimensie met het kleurkanaal weer toe, zodat de vorm nu (28, 28, 1) is.
    afbeelding_array = np.expand_dims(kleurkanaal, axis=-1) #voegt nog een dimensie toe, maar nu aan het begin. deze heeft de grootte van de batch aan. het model verwacht deze vorm omdat modellen getraind worden op meerdere afbeeldingen tegelijk. de vorm van de preprocessed afbeelding die nu klaar is om het model in te gaan, is nu dus (1, 28, 28, 1)
    return(afbeelding_array, resize) #geeft de afbeelding voor in het model terug, en de preprocessed afbeelding om weer te geven op de HTML pagina.
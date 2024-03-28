import tensorflow as tf #AI framework
import numpy as np #voor numpy arrays
import cv2 #voor alle bewerkingen met afbeeldingen
from preprocessing import preprocess #laadt de preprocess functie in, uit preprocessing.py
from model import laadmodel #laadt de functie in die het model inlaadt, uit model.py

#functie die een afbeelding classificeert:
def voorspel(afbeelding): #afbeelding is de afbeelding die de gebruiker uploadt
    preprocessed = preprocess(afbeelding) #gebruikt de preprocess functie op de afbeelding
    preprocessed_voor_model = preprocessed[0] #de eerste index waarde is de numpy array in de vorm die het model verwacht
    preprocessed_afbeelding = preprocessed[1] #de tweede index waarde is 'resize' uit de preprocess functie, dit is de preprocessed afbeelding zonder extra dimensies
    model = laadmodel() #laadt BLUD 11 in
    resultaten = model.predict(preprocessed_voor_model) #voorspelt de waarde van de afbeelding. deze functie geeft een list terug met 10 waardes, voor de 10 klasses. de index van elke klasse die het niet is, is 0 en de klasse die het model wel denkt is 1.
    getal = int(np.argmax(resultaten)) #omdat de cijfers 0 tm 9 geclassificeert worden, is de index met de hoogste waarde ook automatisch het voorspelde cijfer. argmax geeft de hoogste waarde uit een lijst of array terug als numpy int64, die hier wordt omgezet naar een normale python int.
    return getal, preprocessed_afbeelding #deze hele functie geeft dus het voorspelde cijfer terug, en de preprocessed afbeelding.

testt = voorspel('test1.jpg')[0]
print(testt)
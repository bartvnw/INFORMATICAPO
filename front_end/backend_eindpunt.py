import tensorflow as tf #AI framework
import cv2 #bewerkingen met afbeeldingen
import numpy as np #voor numpy arrays
from flask import Flask, jsonify, request
from classificatie import voorspel #voorspelfunctie ophalen vanuit classificatie.py

afbeelding_bestand = #GEBRUIK FLASK OM EEN AFBEELDING OP TE SLAAN
afbeelding = cv2.imdecode(np.frombuffer(afbeelding_bestand.read(), np.uint8), cv2.IMREAD_COLOR) #maakt van de Flask afbeelding een bestand wat opencv kan lezen
resultaat = voorspel(afbeelding) #gebruikt de voorspelfunctie om de afbeelding te classificeren

#resultaat[0] is een integer die terug gestuurd moet worden, en resultaat[1] is een afbeelding als numpy array, die moet denk ik nog omgezet worden voordat shit werkt
#deze 2 moeten allebei terug gestuurd worden naar de server silly :3
import tensorflow as tf #tensorflow is het AI framework wat gebruikt is

#functie die het model inlaadt:
def laadmodel():
    model = tf.keras.models.load_model('blud11.h5') #laadt de 11e en meest recente versie van het model in. BLUD staat voor Brilliant Learning and Understanding Digits
    return model #geeft het model terug als variabele
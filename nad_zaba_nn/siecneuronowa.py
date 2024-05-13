import tensorflow as tf #import do sieci neuronowej
#trzeba dodać tensorflow - pip install tensorflow

#czy genotyp zab w algorytmie genetycznym ma zawierac parametry sieci neuronowej (np wagi polaczen miedzy neuronami?)
 
class siec:
    def __init__(self, dane_wejsciowe, dane_wyjsciowe):
        self.model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=dane_wejsciowe),
            tf.keras.layers.Flatten(), #spłaszczanie danych wejsciowych???
            tf.keras.layers.Dense(128, activation='relu'), #ilosc neuronow
            tf.keras.layers.Dense(64, activation='relu'), #ilosc neuronow
            tf.keras.layers.Dense(dane_wyjsciowe, activation='softmax') #warstwa wyjsciowa (zwraca prawdopodobienstwo)
        ])
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#metoda do trenowania modelu
    def train(self, x_train, y_train, epochs=10): # tu ustawamy ilosc epok
        self.model.fit(x_train, y_train, epochs=epochs)

    def predict(self, observation): #obserwation - obserwacja aktualnego stanu gry
        return tf.argmax(self.model.predict(observation), axis=1).numpy() #zwraca indeks akcji najwyzszym prawdopodobienstwem
import pandas as pd
import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def getData():
    data = pd.read_excel("dadosTrabalhoRNA.xlsx", "Planilha1")
    data.head()
    print(data)
    return data

    validation_data = data.sample(n = 10)
    print(validation_data)
    validation_data.to_csv("validation_data.csv")

    training_data = data.filter(not (lambda x: data.query(validation_data[x])))
    training_data.to_csv("training_data.csv")
    


def getModel():
    model = Sequential()
    """
    model.add(Dense(12, input_shape=(8,), activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    data = getData()
    
    # compile the keras model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(data.Entrada, data.Saida, epochs=150, batch_size=10)
    
    # evaluate the keras model
    _, accuracy = model.evaluate(data.Entrada, data.Saida)
    print('Accuracy: %.2f' % (accuracy*100))
    """

getModel()

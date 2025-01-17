# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12TMGWQbu7aFVNKH6pvVTUxu7Xi-TfXY5
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import time


X = pickle.load(open("X1.pickle", "rb"))
y = pickle.load(open("y1.pickle", "rb"))

X = X/255.0

model = Sequential()
model.add(Conv2D(28, (3,3), input_shape = X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(28, (3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(28))
model.add(Activation('relu'))


model.add(Dense(1))
model.add(Activation('softmax'))

model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ['accuracy'])
model.fit(X, y, epochs = 10, validation_split = 0.2)

model.save('28-CNN1.model')








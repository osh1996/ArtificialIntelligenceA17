from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np


imageFile = "images.npy"
labelFile = "labels.npy"

#Preprocessing Data
imageData = np.load(imageFile) #loads image files
imageData = np.reshape(imageData,(6500, 784)) #reshapes image files into vectors
imageLabel = np.load(labelFile) #loads label files

nb_classes = 10 #goes from 0 - 9 so 10 classes total
hotLabel = to_categorical(imageLabel, nb_classes) #turns labels into hotLabels

#Randomly splitting up data

x, x_Test, y, y_Test = train_test_split(imageData, hotLabel,test_size = 0.25, train_size= 0.75)
x_Train, x_Val, y_Train, y_Val = train_test_split(x, y , test_size = 0.2 ,train_size = 0.8)

# Model Template

model = Sequential() # declare model
model.add(Dense(800, input_shape=(28*28, ), kernel_initializer='he_normal')) # first layer
model.add(Activation('selu'))

model.add(Dense(400))
model.add(Activation('selu'))

model.add(Dense(400))
model.add(Activation('tanh'))


model.add(Dense(10, kernel_initializer='he_normal')) # last layer
model.add(Activation('softmax'))

# Compile Model
model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train Model
history = model.fit(x_Train, y_Train,
                    validation_data = (x_Val, y_Val),
                    epochs=15,
                    batch_size=256,
                    verbose=1)

#saving the model
#model.save('trained_model.h5')

#graphing the model data

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'], loc = 'upper left')
plt.show()

# Report Results

results = model.predict(x_Test, batch_size=1625) #for making the confusion matrix
confusion = np.zeros(shape=(10,10)) #empty confusion matrix

for result in range(1625):
    predicted_label = 0
    actual_label = 0

    max_predicted = 0
    max_actual = 0
    for i in range(10):
        if results[result,i] > max_predicted:
            max_predicted = results[result,i]
            predicted_label = i
    for i in range(10):
        if y_Test[result,i] > max_actual:
            max_actual = y_Test[result,i]
            actual_label = i
    confusion[predicted_label][actual_label] += 1

## PREDICTED LABEL IS Y AXIS OF PRINTED ARRAY

print(confusion)



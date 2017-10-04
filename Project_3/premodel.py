from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np

imageFile = "images.npy"
labelFile = "labels.npy"

#Preprocessing Data
imageData = np.load(imageFile) #loads image files
imageLabel = np.load(labelFile) #loads label files

nb_classes = 10 #goes from 0 - 9 so 10 classes total
flatData = imageData.flatten() #flattens data into a 1D vector
print(flatData.size)
hotLabel = to_categorical(imageLabel, nb_classes) #turns labels into hotLabels
print(hotLabel.size)
#hotLabel = np.eye(nb_classes)[imageLabel]

#Randomly splitting up data
x, x_Test, y, y_Test = train_test_split(flatData,hotLabel,test_size = 0.25, train_size= 0.75)
x_Train, x_Val, y_Train, y_Val = train_test_split(x,y,test_size = 0.2 ,train_size = 0.8)


# Model Template

model = Sequential() # declare model
model.add(Dense(10, input_shape=(28*28, ), kernel_initializer='he_normal')) # first layer
model.add(Activation('relu'))
#
#
#
# Fill in Model Here
#
#
model.add(Dense(10, kernel_initializer='he_normal')) # last layer
model.add(Activation('softmax'))


# Compile Model
model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train Model
history = model.fit(x_Train, y_Train,
                    validation_data = (x_Val, y_Val),
                    epochs=10,
                    batch_size=512,
                    verbose=1) 


# Report Results

print(history.history)
model.predict()
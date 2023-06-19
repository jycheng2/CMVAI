#code based on examples from https://keras.io/


import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

img_width=300
img_height=300
batch_size=64

train_datagen = ImageDataGenerator(

channel_shift_range= 15,
vertical_flip=True,
horizontal_flip=True)

train_data_dir="i:/cmv7b/training/"
val_data_dir="i:/cmv7b/validation/"


val_datagen = ImageDataGenerator(
vertical_flip=True,
horizontal_flip=True                              
                                )


val_ds = val_datagen.flow_from_directory(
   directory=val_data_dir,
   target_size=(img_width, img_height),
   color_mode="rgb",
   batch_size=batch_size,
   shuffle=True,
   class_mode="binary",
   seed=42
 
)

train_ds= train_datagen.flow_from_directory(
directory=train_data_dir,
color_mode="rgb",
target_size=(img_width, img_height),
batch_size=batch_size,
class_mode="binary",
seed=42,
shuffle=True

)

test_data_dir="i:/cmv7b/holdout/"

test_datagen = ImageDataGenerator(
vertical_flip=True,
horizontal_flip=True                              
                                )

test_ds = val_datagen.flow_from_directory(
   directory=test_data_dir,
   target_size=(img_width, img_height),
   color_mode="rgb",
   class_mode="binary",
   batch_size=batch_size,
   shuffle=False,

)

input_shape = (img_width, img_height, 3)
classes = 1
model =tf.keras.applications.EfficientNetV2B0( weights=None, include_top=True, input_shape=input_shape, classes=classes,classifier_activation="sigmoid")

callbacks = [
    
    tf.keras.callbacks.ModelCheckpoint(monitor='accuracy',
    mode='max',
    save_best_only=True,filepath="d:/chkcmv7/EFV2B0scr_save_at_{epoch}_{accuracy}.h5"),
]

model.compile( optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.0001,rho=0.9,momentum=0.0,epsilon=1e-07,centered=False,name="RMSprop" , loss="binary_crossentropy",metrics=["accuracy"] )

model.fit(
    train_ds, batch_size=64,steps_per_epoch=4096,callbacks=callbacks, validation_data=val_ds,epochs=100,validation_batch_size=64
)
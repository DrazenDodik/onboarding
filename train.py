import tensorflow as tf
import json
import argparse
import numpy
import valohai

# Load dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# TODO: Load data
# file_path = ''
#with numpy.load(file_path, allow_pickle=True) as f:
#    x_train, y_train = f['x_train'], f['y_train']
#    x_test, y_test = f['x_test'], f['y_test']

x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
tf.keras.layers.Flatten(input_shape=(28, 28)),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam',
            loss=loss_fn,
            metrics=['accuracy'])

# TODO: Add callback
# metadataCallback = tf.keras.callbacks.LambdaCallback(on_epoch_end=logMetadata)
# model.fit(x_train, y_train, epochs=5, callbacks=[metadataCallback])
model.fit(x_train, y_train, epochs=5)
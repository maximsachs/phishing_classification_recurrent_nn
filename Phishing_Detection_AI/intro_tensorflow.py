import tensorflow as tf
import numpy as np

print(tf.config.list_physical_devices('GPU'))

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Scales input from 0 to 1!
x_train, x_test = np.array(x_train / 255.0, np.float16), np.array(x_test / 255.0, np.float16)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=8)

model.evaluate(x_test,  y_test, verbose=2)
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib as mlt
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import sklearn
import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing
houseing = fetch_california_housing()

x_train_all, x_test, y_train_all, y_test = train_test_split(
    houseing.data, houseing.target, random_state=7
)

# 从训练集中划分出来的验证集
x_train, x_valid, y_train, y_valid = train_test_split(
    x_train_all, y_train_all, random_state=11
)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_valid_scaled = scaler.fit_transform(x_valid)
x_test_scaled = scaler.fit_transform(x_test)


input_wide = keras.layers.Input(shape=[5])
input_deep = keras.layers.Input(shape=[6])
# 开发隐藏层的设计
hidden1 = keras.layers.Dense(30, activation="relu")(input_deep)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)
concat = keras.layers.concatenate([input_wide, hidden2])
output = keras.layers.Dense(1)(concat)

# 阔化的操作
model = keras.models.Model(inputs=[input_wide, input_deep], outputs=output)
model.compile(loss="mse", optimizer="sgd")

callbacks = [keras.callbacks.EarlyStopping(patience=5, min_delta=1e-2)]
model.summary()

# x_train_scaled_wide
x_train_scaled_wide = x_train_scaled[:, :5]
x_train_scaled_deep = x_train_scaled[:, 2:]
x_valid_scaled_wide = x_valid_scaled[:, :5]
x_valid_scaled_deep = x_valid_scaled[:, 2:]
x_test_scaled_wide = x_test_scaled[:, :5]
x_test_scaled_deep = x_test_scaled[:, 2:]

history = model.fit([x_train_scaled_wide, x_train_scaled_deep], y_train,
                    validation_data=(
    [x_valid_scaled_wide, x_valid_scaled_deep], y_valid
),
    epochs=10,
    callbacks=callbacks
)


def plot_learn_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 1)
    plt.show()


# plot_learn_curves(history)
print(model.predict([x_valid_scaled_wide, x_valid_scaled_deep]))
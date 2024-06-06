import tensorflow as tf
from tensorflow import keras
import numpy as np

# numList와 fee 예시 데이터
numList = [1, 2, 3, 4, 5]
fee = [2.0, 4.1, 6.1, 8.3, 10.2]

# numpy array로 변환
numListpy = np.array(numList, dtype=np.float32)
feepy = np.array(fee, dtype=np.float32)

# 모델 정의
model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

# 모델 컴파일
model.compile(optimizer='sgd', loss='mean_squared_error')

# 학습 횟수를 변수 a에 저장
a = 0

class CustomCallback(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        global a
        a += 1
        print(f"Epoch {epoch + 1}: Variable a is now {a}")

# 모델 학습
model.fit(numListpy, feepy, epochs=100, callbacks=[CustomCallback()])

# 새로운 입력 데이터로 예측
resultNum = np.array([len(numList) + 1], dtype=np.float32)
resultFee = model.predict(resultNum)

print(f"The predicted fee for the next number {len(numList) + 1} is: {resultFee[0][0]:.2f}")

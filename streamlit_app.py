import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 폐루프 전달함수의 분자와 분모 계수를 설정합니다.
num = [100]
den = [1, 5, 106]

# 폐루프 전달함수의 전달함수 객체를 생성합니다.
sys = signal.TransferFunction(num, den)

# 응답 시간 범위를 설정합니다.
t = np.linspace(0, 10, 1000)

# unit step 입력에 대한 응답을 계산합니다.
t, y = signal.step(sys, T=t)

# 그래프를 그립니다.
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Step Response of L(s) = 100 / (s^2 + 5s + 106)')
plt.grid(True)
plt.show()

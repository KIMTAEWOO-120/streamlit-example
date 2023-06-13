import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st

# 애플리케이션 제목
st.title("unit step 입력의 응답곡선")


# 폐루프 전달함수의 분자와 분모 계수를 설정합니다.
num = [100]
den = [1, 5, 106]

# 폐루프 전달함수의 전달함수 객체를 생성합니다.
sys = signal.TransferFunction(num, den)

# 응답 시간 범위를 설정합니다.
t = np.linspace(0, 10, 1000)

# unit step 입력에 대한 응답을 계산합니다.
t, y = signal.step(sys, T=t)

# Streamlit 앱을 생성합니다.
st.title('Step Response')
st.line_chart(y, use_container_width=True) 

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st


# 애플리케이션 제목
st.title("주파수 응답")


# 폐루프 전달함수의 분자와 분모 계수를 설정합니다.
num = [100]
den = [1, 5, 106]

# 폐루프 전달함수의 전달함수 객체를 생성합니다.
sys = signal.TransferFunction(num, den)

# 보드선도를 그립니다.
w, mag, phase = signal.bode(sys)

# 주파수 응답 그래프를 그립니다.
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.semilogx(w, mag)
ax1.set_xlabel('Frequency [rad/s]')
ax1.set_ylabel('Magnitude [dB]')
ax1.set_title('Bode Plot - Magnitude')

ax2.semilogx(w, phase)
ax2.set_xlabel('Frequency [rad/s]')
ax2.set_ylabel('Phase [degrees]')
ax2.set_title('Bode Plot - Phase')

plt.tight_layout()

# Streamlit 앱을 생성합니다.
st.title('Bode Plot')
st.pyplot(fig)

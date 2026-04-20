import numpy as np
import matplotlib.pyplot as plt

# -------- CASO 1 --------
fs1 = 1000
t1 = np.linspace(0, 1, fs1, endpoint=False)
x1 = np.sin(2*np.pi*40*t1)

N1 = len(x1)
X1 = np.fft.fft(x1)
f1 = np.fft.fftfreq(N1, 1/fs1)

# -------- CASO 2 --------
fs2 = 8000
t2 = np.linspace(0, 1, fs2, endpoint=False)
x2 = np.sin(2*np.pi*40*t2)

N2 = len(x2)
X2 = np.fft.fft(x2)
f2 = np.fft.fftfreq(N2, 1/fs2)

# Solo frecuencias positivas
mitad1 = N1 // 2
mitad2 = N2 // 2

f1_pos = f1[:mitad1]
mag1 = np.abs(X1[:mitad1]) * 2 / N1

f2_pos = f2[:mitad2]
mag2 = np.abs(X2[:mitad2]) * 2 / N2

# -------- GRÁFICAS --------
plt.figure(figsize=(12, 10))

# Señales en el tiempo
plt.subplot(2,1,1)
plt.plot(t1, x1, label="Fs = 1000 Hz")
plt.plot(t2, x2, '--', label="Fs = 8000 Hz")
plt.title("Comparación en el Tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)

# FFT
plt.subplot(2,1,2)
plt.stem(f1_pos, mag1, linefmt='blue', markerfmt='bo', basefmt=" ", label="Fs = 1000 Hz")
plt.stem(f2_pos, mag2, linefmt='red', markerfmt='ro', basefmt=" ", label="Fs = 8000 Hz")

plt.title("Comparación FFT")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.xlim(0, 100)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

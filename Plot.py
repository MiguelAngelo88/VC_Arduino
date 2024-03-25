import serial
from matplotlib import pyplot as plt
import numpy as np

ser = serial.Serial('COM4', 115200)

plt.title('Dados enviados pelo Arduino')
plt.close('all')
plt.ion()
plt.figure()
plt.show()

i = 0

dados = np.array([])

while True:

    dados_novos = ser.readline()
    dados_novos.decode()
    b = int(dados_novos)
    dados = np.append(dados, b)
    plt.cla()
    plt.plot(dados)

    i += 1
    plt.pause(0.001)

'''
 Blog Eletrogate - Como conectar o Arduino com Python
 Miguel Sena
 blog.eletrogate.com
'''

import serial #Importa a biblioteca
import time
import matplotlib.animation as animation
from datetime import datetime
import matplotlib.pyplot as plt 
contagem = []
horario = []
# Creating the Figure instance 

# showing the plot 

while True: #Loop para a conexão com o Arduino
 
    arduino = serial.Serial(port='COM3', baudrate=115200)
    print('Arduino conectado')
    break

x = []
y = []
count = 0
# to run GUI event loop

# here we are creating sub plots
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i, x, y):

    text = arduino.readline().decode().replace('\r\n', '\n')
    print(text)
    if 'contagem' in text:
        now = datetime.now().strftime('%H:%M:%S.%f')
        print(text)
        contagem = int(text.split('contagem: ')[1])


        x.append(contagem)
        y.append(now)
            
    # Draw x and y lists
        x = x[-4:]
        y = y[-4:]
        with open("banco_de_dados", 'a') as file1:
            file1.write(f"{contagem},{now}\n")
        ax.set_title('Contagem de Movimento')
        ax.clear()
        ax.plot(y, x)


  
        # update scatter data


ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=1000)
plt.show()
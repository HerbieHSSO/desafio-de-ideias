'''
 Blog Eletrogate - Como conectar o Arduino com Python
 Miguel Sena
 blog.eletrogate.com
'''

import serial #Importa a biblioteca

import plotly.graph_objects as go 
  
x = []
y = []
# Creating the Figure instance 
f = go.FigureWidget()  
  
# showing the plot 
f
f.add_scatter(y=y)
while True: #Loop para a conexão com o Arduino
 
    arduino = serial.Serial(port='COM3', baudrate=115200)
    print('Arduino conectado')
    break

   

while True: #Loop principal
    text = arduino.readline().decode().replace('\r\n', '\n')
    print(text)
    if 'contagem' in text:
      
        y.append(int(text.split('contagem: ')[1]))
        # update scatter data
        scatter = f.data[0]
        scatter.y = [3, 1, 4, 3]



import csv

with open('projeto.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["bic", "contagem", "horario"]
    
    writer.writerow(field)
    writer.writerow(["TBUT 0112", "40", "18:49"])
    writer.writerow(["OPPS 9883", "23", "19:30"])
    writer.writerow(["GHGJ 8920", "50", "19:40"])
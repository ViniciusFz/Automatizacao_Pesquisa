import matplotlib.pyplot as plt
import csv
import numpy as np

x = 2

tempoCh1=[]
tensaoCh1=[]
tempoCh2=[]
tensaoCh2=[]

#Descrever o nome do arquivo
filenameCH1 = 'ALL000'+str(x)+'\F000'+str(x)+'CH1.csv'
filenameCH2 = 'ALL000'+str(x)+'\F000'+str(x)+'CH2.csv'


with open(filenameCH1, 'rt') as f:
	reader = csv.reader(f)
	for row in reader:
		tempoCh1.append(float(row[3]))
		tensaoCh1.append(float(row[4]))

with open(filenameCH2, 'rt') as f:
	reader = csv.reader(f)
	for row in reader:
		tempoCh2.append(float(row[3]))
		tensaoCh2.append(float(row[4]))
		
		
print(tensaoCh2)

Pico = max(tensaoCh2)
print("Pico = ",Pico)
Final = tensaoCh1[-1]
print("Estabiliza em  = ",tensaoCh2[-1])
SobreSinal = 100*(Pico-Final)/Final
print("SobreSinal = ",SobreSinal,"%")
Erro = (1-tensaoCh2[-1])*100
print("Erro = ",Erro,"%")

# Começa a montar o primeiro gráfico
plt.figure()

plt.plot(tempoCh2,tensaoCh2,label='Vout(CH2); MP = '+str(round(SobreSinal,3))+'%; Erro = '+str(round(Erro,1))+'%' )
plt.plot(tempoCh1, tensaoCh1,label='Vin(CH1)  = '+str(max(tensaoCh1))+'Vmax')                    # Bode magnitude plot

plt.title('Resposta a degrau')                  # Titulo
plt.ylabel('Tensão [V]')        # Plota o label y
plt.xlabel('Tempo [s]')            # Plota o label x
plt.grid(which='both', axis='both')     # Gride para frequências intermediárias
plt.grid(True)                          # Mostra o Grid
plt.margins(0, 0.1)                     # Deixa uma margem
plt.legend()
plt.savefig('degrau.png')


plt.show()   

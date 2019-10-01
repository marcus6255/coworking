'''
Gráfico
'''

#import pandas as pd
import matplotlib.pyplot as plt


x=pd.read_excel(r"C:\Users\Marcelo\Desktop\grafico1.xlsx")

plt.style.use()
plt.plot (x["Nota"])
plt.show()

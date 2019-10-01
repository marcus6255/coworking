import pandas as pd
import matplotlib.pyplot as plt
import xlrd

x= pd.read_excel(r"C:\Users\Marcelo\Desktop\grafico1.xlsx")

#print(x.head())
plt.hist (x["Nota"])
plt.show()

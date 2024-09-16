import os

import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "data.csv")
df = pd.read_csv(csv_path)

# Gráfico de líneas
ventas_mes = df.groupby(['Mes'], sort=False).sum()
grafico_matplotlib_lineas = ventas_mes.plot(y='Unidades')
grafico_datapane_lineas = dp.Plot(grafico_matplotlib_lineas, responsive=False)


#Gráfico de barras
ventas_vendedor = df.groupby(['Nombre']).sum()
grafico_matplotlib_barras = ventas_vendedor.plot.bar(y='Importe (€)')
#Este método permite que no se corten las etiquetas de los nombres de los vendedores
# plt.tight_layout()
grafico_datapane_barras = dp.Plot(grafico_matplotlib_barras, responsive=False)


#Gráfico de sectores
grafico_matplotlib_sectores = ventas_vendedor.plot.pie(y='Unidades',legend=False, ylabel="")
grafico_datapane_sectores = dp.Plot(grafico_matplotlib_sectores, responsive=False)

report = dp.Report(grafico_datapane_lineas,grafico_datapane_barras,grafico_datapane_sectores)
report_path = os.path.join(base_path, "grafics.html")
report.save(path=report_path, open=True)
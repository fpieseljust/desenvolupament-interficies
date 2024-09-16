import os

import datapane as dp
import pandas as pd

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "data.csv")
df = pd.read_csv(csv_path)

datos_diciembre = df[df['Mes'] == 'Diciembre']
unidades_diciembre = datos_diciembre['Unidades'].sum()

datos_noviembre = df[df['Mes'] == 'Noviembre']
unidades_noviembre = datos_noviembre['Unidades'].sum()

unidades = dp.BigNumber(heading='Unidades totales en diciembre',
                        value=unidades_diciembre,
                        change=unidades_diciembre - unidades_noviembre,
                        is_upward_change=unidades_diciembre > unidades_noviembre)
report = dp.Report(unidades)
report_path = os.path.join(base_path, "informe3.html")
report.save(path=report_path, open=True)

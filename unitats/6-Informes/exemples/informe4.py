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

titulo = dp.HTML('''
<p style="font-size:30px;text-align:center;color:#ffffff;background-color:#4d4d4d;">
    Informe de ventas
</p>''')
data_path = os.path.join(base_path, "data.csv")
fichero = dp.Attachment(file=data_path)
texto = dp.Text('**Puedes descargar el fichero con los datos del informe.**')
image_path = os.path.join(base_path, "img", "report.png")
imagen = dp.Media(file=image_path)

report = dp.Report(imagen, titulo, unidades, texto, fichero)
report_path = os.path.join(base_path, "informe4.html")
report.save(path=report_path, open=True)

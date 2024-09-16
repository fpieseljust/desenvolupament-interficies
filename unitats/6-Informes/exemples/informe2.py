import os

import datapane as dp
import pandas as pd

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "data.csv")
df = pd.read_csv(csv_path)

table = dp.Table(df)
data_table = dp.DataTable(df)
report = dp.Report(table, data_table)
report_path = os.path.join(base_path, "informe2.html")
report.save(path=report_path, open=True)
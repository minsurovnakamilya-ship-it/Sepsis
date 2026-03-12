import pandas as pd

file_path = "Dataset.csv"
data = pd.read_csv(file_path)

# Отключаем все ограничения pandas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(data)
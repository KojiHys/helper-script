import pandas as pd

# pip install pandas
# pip install openpyxl
# version 0.2

# CSVファイルの名前とパスをリストに追加します
csv_files = ['file1.csv', 'file2.csv', 'file3.csv']

# 出力するExcelファイルの名前とパスを設定します
output_file = 'merged.xlsx'

# マージに使用するカラム名をリストに追加します
selected_columns = ['id', 'column1', 'column2']

# 最初のCSVファイルを読み込みます
merged_data = pd.read_csv(csv_files[0])

# 残りのCSVファイルを読み込み、選択されたカラムだけを残し、マージします
for file in csv_files[1:]:
    data = pd.read_csv(file)
    data = data[selected_columns]
    merged_data = merged_data.merge(data, on='id', how='outer')

# マージされたデータをExcelファイルに書き込みます
merged_data.to_excel(output_file, index=False, engine='openpyxl')

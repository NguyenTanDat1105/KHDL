import pandas as pd
data_file_path = "BangCanNang.xlsx"
health_df = pd.read_excel(data_file_path)

print(health_df)
print(health_df.describe())
# Bo sung cot moi co ten bmi chua chi so BMI tuong ung
health_df['bmi'] = health_df.apply(lambda row: row["bmi"]/row["height"], axis=1)


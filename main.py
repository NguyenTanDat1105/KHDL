# Doc file Excel
import pandas as pd

# path to the data file
# data_file_path = r"C:\Users\ACER\PycharmProjects\KHDL\Book1.xlsx"
# data_file_path = r"C:\Users\ACER\OneDrive\Documents\Book1.xlsx"
data_file_path = r"C:\Users\ACER\Downloads\car-sales-extended-missing-data.csv"
carsales_df = pd.read_csv(data_file_path)

print(carsales_df)
print(carsales_df.describe())
carsales_df.info()
print("Loai bo cac dong toi thieu tren df hien tai:")
print(carsales_df.dropna(inplace=True))
print("ISMA: ")
print(carsales_df.isna().sum())


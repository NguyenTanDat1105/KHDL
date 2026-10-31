import matplotlib
import matplotlib.pyplot as plt

# 1. Kiểm tra phiên bản
print(f"Current version: {matplotlib.__version__}")

# 2. Khai báo dữ liệu mẫu
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [10, 15, 12, 18, 25]

# 3. Vẽ biểu đồ
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Units (Ty VND)")
plt.grid(alpha=0.3)

# 4. Hiển thị biểu đồ
# Save the plot to disk (must be done before the show() function)
plt.savefig(r'C:\Users\ACER\Downloads\sales-data.pdf')
plt.show()

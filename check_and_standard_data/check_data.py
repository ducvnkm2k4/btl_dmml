import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Tạo DataFrame mẫu
data = pd.read_csv('data\\diabetes.csv')
df = pd.DataFrame(data)

# Tính ma trận tương quan
correlation_matrix = df.corr()

# Vẽ heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

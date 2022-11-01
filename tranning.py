import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

#  đọc file dữ liệu được chuyển đổi:
data = pd.read_csv('bank-data_xuly.csv', index_col="id")

# Xét các thuộc tính đánh giá
features = ['age', 'sex', 'region', 'income', 'married', 'children', 'car', 'save_act', 'current_act', 'mortgage']

# x là thuộc tính xét, y là kết quả
x = data[features]
y = data["pep"]
y = y.astype('int')

# chia ngẫu nhiên tập train và tập test theo tỷ lệ 8-2
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

# train mô hình
classifer = svm.SVC()
classifer.fit(x_train, y_train)

# thu thập kết quả dự đoán
predicted = classifer.predict(x_test)

#  so sánh kết quả dự đoán với kết quả test
print(metrics.classification_report(y_test, predicted))

# Hình ảnh kết quả
metrics.plot_confusion_matrix(classifer, x_test, y_test)

plt.title('Kết quả')
plt.show()

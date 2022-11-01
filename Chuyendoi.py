import pandas as pd

# Hàm chuyển dạng chữ sang số
def convert(A):
  B=list(set(A))
  n= len(A)
  m= len(B)
  for i in range(n):
    for j in range(m):
      if A[i]==B[j]:
        A[i]=j
  return B
# Đọc bank-data
data = pd.read_csv('bank-data.csv',index_col = "id")
need_convert= [ 'sex', 'region','married', 'car', 'save_act', 'current_act', 'mortgage','pep']
B=[] # lưu lại giá trị của côt  tương ứng với index
for i in need_convert:
  B.append(convert(data[i]))
# Lưu file đã chuyển đổi
data.to_csv('bank-data_xuly.csv')
pd.DataFrame(B).to_csv('convert_data.csv')
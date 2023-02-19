import pandas as pd

# Membaca data dari file CSV
def convert():
    data = pd.read_csv('dataset-pkh.csv')

    # Menyimpan data ke file Excel baru
    data.to_excel('dataset-pkh.xlsx', index=False)

def convert1():
    # membaca file dataset-bpnt.xlsx
    df1 = pd.read_excel("dataset-bpnt.xlsx", header=0, usecols="A:M")

    # membaca file dataset-pkh.xlsx
    df2 = pd.read_excel("dataset-pkh.xlsx", header=0, usecols="M")

    # menggabungkan kedua dataset
    df3 = pd.concat([df1, df2], axis=1)

    # menyimpan hasil gabungan ke dalam file3.xlsx
    df3.to_excel("file3.xlsx", index=False)

    # Menyimpan hasil gabungan ke file 'file3.xlsx'
    df3.to_excel('file3.xlsx', index=False)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Membaca data dari file excel
data = pd.read_excel("data_gabungan.xlsx")

# Memisahkan data menjadi atribut dan label
X = data.drop(["class_bpnt", "class_pkh"], axis=1)
y_bpnt = data["class_bpnt"]
y_pkh = data["class_pkh"]

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_bpnt_train, y_bpnt_test = train_test_split(X, y_bpnt, test_size=0.3, random_state=0)
X_train, X_test, y_pkh_train, y_pkh_test = train_test_split(X, y_pkh, test_size=0.3, random_state=0)

# Membuat objek Naive Bayes
gnb_bpnt = GaussianNB()
gnb_pkh = GaussianNB()

# Melatih model
gnb_bpnt.fit(X_train, y_bpnt_train)
gnb_pkh.fit(X_train, y_pkh_train)

# Membuat prediksi
y_bpnt_pred = gnb_bpnt.predict(X_test)
y_pkh_pred = gnb_pkh.predict(X_test)

# Mencetak akurasi
print("Akurasi prediksi class_bpnt:", accuracy_score(y_bpnt_test, y_bpnt_pred))
print("Akurasi prediksi class_pkh:", accuracy_score(y_pkh_test, y_pkh_pred))

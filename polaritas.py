import pandas as pd

# Gantilah 'nama_file.csv' dengan nama file CSV yang berisi data analisis dan kolom sentimen
file_path = 'labelling.csv'

# Membaca data dari file CSV menggunakan pandas
data = pd.read_csv(file_path)

# Menghitung jumlah sentimen untuk setiap kategori
sentimen_counts = data['labelling'].value_counts()

# Menampilkan hasil di terminal
print("Jumlah sentimen:")
print(sentimen_counts)
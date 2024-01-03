import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline

# Load data CSV
file_path = 'labelling.csv'  # Ganti dengan path file CSV Anda
data = pd.read_csv(file_path)

# Hapus baris yang memiliki nilai kosong
data = data.dropna()

# Bagi dataset menjadi data latih dan data uji
train_data, test_data, train_labels, test_labels = train_test_split(
    data['Hasil_Kalimat'], data['labelling'], test_size=0.2, random_state=42
)

# Menampilkan jumlah data uji dan data latih
print(f'Jumlah Data Latih: {len(train_data)}')
print(f'Jumlah Data Uji: {len(test_data)}')

# Buat model Naive Bayes menggunakan pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(train_data, train_labels)

# Lakukan prediksi pada data uji
predictions = model.predict(test_data)

# Evaluasi model
accuracy = accuracy_score(test_labels, predictions)
report = classification_report(test_labels, predictions)

# Tampilkan hasil evaluasi
print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{report}')

# Menambahkan prediksi ke dalam dataframe
test_data_with_predictions = pd.DataFrame({'Comment': test_data, 'True_Label': test_labels, 'Predicted_Label': predictions})

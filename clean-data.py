import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load data CSV
file_path = 'youtube-comments-data1.csv'  # Ganti dengan path file CSV Anda
data = pd.read_csv(file_path)

# Hapus baris yang memiliki nilai kosong
data = data.drop(['publishedAt'], axis=1)
data = data.dropna()

# Fungsi untuk membersihkan, case folding, tokenizing, dan stopword
def preprocess_text(text):
    # Cleansing data: Menghapus karakter yang tidak diinginkan (misalnya, simbol, angka)
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Case folding: Mengonversi teks menjadi huruf kecil
    lowered_text = cleaned_text.lower()

    # Tokenizing
    tokens = word_tokenize(lowered_text)

    # Stopword removal
    stop_words = set(stopwords.words('indonesian'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    return {
        'Text_Display': text,
        'Cleansed_Text': cleaned_text,
        'Case_Folding': lowered_text,
        'Tokenized_Text': tokens,
        'Stopwords': filtered_tokens,
        'Hasil_Kalimat': ' '.join(filtered_tokens)
    }

# Preprocess teks pada kolom komentar
data['preprocessed_details'] = data['textDisplay'].apply(preprocess_text)

# Membuat DataFrame dari hasil preprocessing
preprocessed_data = pd.DataFrame(data['preprocessed_details'].tolist())

# Menyimpan hasil preprocessing ke dalam file CSV
preprocessed_file_path = 'preprocessed-data.csv'
preprocessed_data.to_csv(preprocessed_file_path, index=False)

print(f'Data yang telah dipreprocessing disimpan di: {preprocessed_file_path}')

# Tampilkan beberapa hasil preprocessing
print("\nBeberapa hasil preprocessing:")
print(preprocessed_data.head(5))

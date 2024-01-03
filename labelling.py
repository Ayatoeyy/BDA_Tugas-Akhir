import pandas as pd

def load_sentiment_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return set(words)

def label_sentiment(comment, positive_words, negative_words):
    # Penanganan nilai NaN
    if isinstance(comment, float):
        return 'netral'

    positive_count = sum(1 for word in comment.split() if word.lower() in positive_words)
    negative_count = sum(1 for word in comment.split() if word.lower() in negative_words)

    if positive_count > negative_count:
        return 'positif'
    elif positive_count < negative_count:
        return 'negatif'
    else:
        return 'netral'

# Load positive and negative word dictionaries
positive_words_path = 'positive.txt'  # Ganti dengan path kamus kata positif
negative_words_path = 'negative.txt'  # Ganti dengan path kamus kata negatif

positive_words = load_sentiment_dictionary(positive_words_path)
negative_words = load_sentiment_dictionary(negative_words_path)

# Load data komentar YouTube berbahasa Indonesia
comments_path = 'preprocessed-data.csv'  # Ganti dengan path data komentar Anda
comments_data = pd.read_csv(comments_path)

# Melabeli sentimen komentar
comments_data['labelling'] = comments_data['Hasil_Kalimat'].apply(
    lambda x: label_sentiment(x, positive_words, negative_words)
)

# Simpan hasil labeling ke dalam file CSV
output_path = 'labelling.csv'  # Ganti dengan path file output Anda
comments_data.to_csv(output_path, index=False)

print(f'Data yang telah dilabeli disimpan di: {output_path}')

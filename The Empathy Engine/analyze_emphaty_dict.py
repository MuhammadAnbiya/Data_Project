# Step 1: Membuat sebuah variabel bernama words dengan type dictionary yang isinya sebuah list kata-kata positif dan kata-kata negatif
words = {
    "positive_words": [
        "hangat", "bahagia", "spesial", "senang", "cinta", "hebat", "luar biasa", 
        "sukses", "bangga", "bersyukur", "damai", "ceria", "semangat", "optimis", 
        "impian", "berarti", "koneksi", "tenang", "berkembang", "tumbuh", "asik", 
        "nyaman", "keajaiban", "berharga", "berhasil", "kuat", "semangat", "percaya"
    ],
    "negative_words": [
        "sedih", "kesepian", "kecewa", "sakit", "sendiri", "gagal", "lelah", 
        "bimbang", "ragu", "cemas", "stres", "hampa", "terluka", "hilang", 
        "buruk", "menderita", "marah", "takut", "kosong", "tertekan", "lemah", 
        "rumit", "kacau", "menyesal", "ditinggalkan", "suram"
    ]
}

# Step 2: Text Pre-Processing (Tokenization)
# Komputer membaca teks sebagai satu kesatuan, kamu perlu memecahnya.
def clean_and_tokenize(text):
    clean_text = text.lower().replace('.','').replace(',','').split()
    return clean_text


# Step 3; The Scoring Logic
def analyze_sentiment(sentence):
    clean_sentence = clean_and_tokenize(sentence)
    score = 0
    result = ""
    
    for text in clean_sentence:
        if text in words["positive_words"]:
            score += 1
        elif text in words["negative_words"]:
            score -= 1

        # OLD ALGORITHM
        # for pos_word in words["positive_words"]:
        #     if text == pos_word:
        #         score += 1
        # for neg_word in words["negative_words"]:        
        #     if text == neg_word:
        #         score -= 1

    # Steps 4: Decision Making
    # Menentukan Threshold
    if score > 0:
        result = "Output: Sentimen Positif (Hangat)"
    elif score < 0:
        result = "Output: Sentimen Negatif (Perlu semangat)"
    else:
        result = "Output: Netral"
    return result


text = input("Masukan Kalimat yang Ingin di Analisis :")
print(analyze_sentiment(text))
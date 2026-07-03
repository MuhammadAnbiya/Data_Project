"""
=========================================================
STUDY CASE: THE TEXT SENTIMENT ORACLE
=========================================================
[KETERANGAN SOAL]
Naive Bayes adalah algoritma probabilitas yang sangat handal untuk klasifikasi teks.
Di sini, Anda akan membuat model yang dapat menebak apakah sebuah kalimat/ulasan
bersentimen POSITIF (1) atau NEGATIF (0) berdasarkan frekuensi kemunculan tiap kata.

[EKSPEKTASI HASIL]
1. Kode dapat membersihkan kalimat dan memecahnya menjadi daftar kata (tokenization).
2. Kode dapat menghitung probabilitas Prior: P(Positif) dan P(Negatif).
3. Kode dapat menghitung frekuensi kemunculan (Likelihood): P(Kata | Positif).
4. Tes prediksi pada ulasan baru: "kualitas bagus sekali" harus diprediksi Positif (1).

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: PERSIAPAN DATASET
- Buat dua list (atau load dari dataset.txt):
  X_train = ["bagus sekali", "jelek banget", "sangat bagus", "buruk sekali"]
  y_train = [1, 0, 1, 0]

STEP 2: PREPROCESSING TEKS
- Gunakan/Import fungsi `clean_text` dari file `utils.py` yang sudah disediakan.
- Pisahkan (split) setiap kalimat menjadi list kata-kata (words) menggunakan `.split()`.

STEP 3: MENGHITUNG PRIOR (PROBABILITAS KELAS AWAL)
- Buat fungsi `calculate_prior(y_train)`.
- Hitung persentase kemunculan kelas 1 dan kelas 0 di dataset.
- Prior(1) = jumlah kelas 1 / total data. 
- Prior(0) = jumlah kelas 0 / total data.

STEP 4: MENGHITUNG KEMUNCULAN KATA (WORD FREQUENCIES)
- Buat dictionary (misal `word_counts`) untuk menghitung seberapa sering sebuah kata muncul di kelas 1 maupun kelas 0.
- Contoh bentuk dictionary-nya: {"bagus": {1: 2, 0: 0}, "jelek": {1: 0, 0: 1}}

STEP 5: PREDIKSI (TEOREMA BAYES DENGAN LAPLACE SMOOTHING)
- Buat fungsi `predict(text, word_counts, prior_1, prior_0)`.
- Bersihkan `text` baru tersebut dan pecah jadi kata-kata.
- Hitung total skor probabilitas untuk kelas 1 dan kelas 0.
- Ingat gunakan 'Laplace Smoothing' (tambah 1 ke frekuensi kemunculan kata) agar tidak terjadi perkalian dengan 0.
- Bandingkan skor kelas 1 dan kelas 0, return (kembalikan) angka kelas yang skor probabilitasnya lebih tinggi.

STEP 6: EKSEKUSI & UJI COBA
- Tulis kode uji coba di baris paling bawah.
- Latih modelnya (jalankan Step 3 dan Step 4).
- Coba prediksi teks: "produk ini sangat buruk dan jelek" (Harus return 0).
- Coba prediksi teks: "kualitas bagus sekali" (Harus return 1).
"""

# MULAI KODING DI BAWAH SINI:


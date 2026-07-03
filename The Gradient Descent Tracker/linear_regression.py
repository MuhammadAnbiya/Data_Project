"""
=========================================================
STUDY CASE: THE GRADIENT DESCENT TRACKER
=========================================================
[KETERANGAN SOAL]
Di dunia Machine Learning, Gradient Descent adalah algoritma optimasi utama yang digunakan untuk melatih model dengan meminimalkan error. 
Tugas Anda hari ini adalah membuat sebuah "Line Fitter" (Linear Regression) sederhana dari nol menggunakan pure Python (tanpa library ML).
Model ini akan memprediksi Gaji (Salary) dalam Juta Rupiah berdasarkan Pengalaman Kerja (Years of Experience).

[EKSPEKTASI HASIL]
1. Kode dapat berjalan dan melakukan proses "training" (perulangan/epochs) di mana nilai error (cost) semakin menurun seiring berjalannya epoch.
2. Parameter 'w' (weight) dan 'b' (bias) yang dihasilkan akan membentuk persamaan garis yang merepresentasikan pola data.
3. Anda dapat melakukan tes prediksi pada data baru: Jika pengalaman kerja (x) adalah 6.0 tahun, hasil prediksi gaji (y) harus mendekati 15.0 juta.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: DEKLARASI DATASET
- Buat variabel list untuk menyimpan data latih.
- x_data (Years of Experience): 1.0, 2.0, 3.0, 4.0, 5.0
- y_data (Salary): 5.0, 7.0, 9.0, 11.0, 13.0

STEP 2: FUNGSI PREDIKSI (HYPOTHESIS)
- Buat fungsi, misalnya `predict(x, w, b)`.
- Fungsi ini mengembalikan hasil dari persamaan garis lurus linear: (w * x + b).

STEP 3: FUNGSI COST / LOSS (MEAN SQUARED ERROR)
- Buat fungsi, misalnya `compute_cost(y_true, y_pred)`.
- Fungsi ini menghitung rata-rata kuadrat selisih antara tebakan dan data asli.
- Rumus MSE: L = (1 / N) * sum( (y_pred - y_true)^2 )
- N adalah panjang/jumlah data.

STEP 4: FUNGSI GRADIENT (TURUNAN PARSIAL)
- Buat fungsi, misalnya `compute_gradients(x, y_true, y_pred)`.
- Hitung dua turunan (gradient) ini menggunakan loop untuk mencari arah perubahan parameter.
- Rumus dw = (2 / N) * sum( (y_pred - y_true) * x )
- Rumus db = (2 / N) * sum( (y_pred - y_true) )
- Kembalikan nilai dw dan db.

STEP 5: TRAINING LOOP (GRADIENT DESCENT)
- Buat fungsi utama, misalnya `train(x, y, epochs, learning_rate)`.
- Inisialisasi parameter awal: w = 0.0, b = 0.0.
- Buat perulangan (for loop) sebanyak `epochs`.
- Di dalam perulangan tersebut:
   a. Lakukan prediksi (STEP 2) untuk seluruh data x.
   b. Hitung gradients dw dan db (STEP 4).
   c. Hitung nilai cost (STEP 3) dan cetak (print) nilainya di terminal setiap 100 epoch agar terlihat progresnya.
   d. Lakukan update parameter w dan b:
      w = w - (learning_rate * dw)
      b = b - (learning_rate * db)
- Jika loop selesai, return nilai w dan b yang sudah terlatih.

STEP 6: EKSEKUSI & UJI COBA
- Tulis blok pengeksekusian kode di bagian paling bawah.
- Tentukan epochs (misalnya: 1000) dan learning_rate (misalnya: 0.01).
- Panggil fungsi training (STEP 5) dengan dataset x_data dan y_data.
- Setelah mendapat w dan b akhir, cetak persamaannya.
- Lakukan pengujian: Hitung gaji untuk seseorang dengan x = 6.0 tahun, lalu print hasilnya.
"""

# MULAI KODING DI BAWAH SINI:

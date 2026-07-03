"""
=========================================================
STUDY CASE: THE KNN MATCHMAKER
=========================================================
[KETERANGAN SOAL]
Algoritma K-Nearest Neighbors (KNN) adalah algoritma Machine Learning yang sangat intuitif untuk klasifikasi. 
Prinsipnya: "Katakan padaku siapa tetanggamu, maka aku akan tahu siapa dirimu."
Tugas Anda hari ini adalah membuat model KNN dari nol menggunakan pure Python (tanpa library).
Model ini akan memprediksi apakah seorang user akan "Suka" (1) atau "Tidak Suka" (0) terhadap sebuah produk/film, 
berdasarkan kemiripan Umur (Age) dan Skor Ketertarikan (Interest Score) mereka dengan user lain.

[EKSPEKTASI HASIL]
1. Kode dapat menghitung jarak (Euclidean Distance) antar dua user (berdasarkan fitur Umur dan Skor).
2. Kode dapat mencari K tetangga terdekat dari seorang user baru.
3. Kode dapat melakukan "Voting" untuk menentukan kelas user baru tersebut berdasarkan mayoritas kelas tetangganya.
4. Tes prediksi pada user baru berumur 25 dengan skor 8.0 harus menghasilkan prediksi kelas yang tepat dan tidak error.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: DEKLARASI DATASET
- Buat sekumpulan data latih (variabel list of lists/tuples) yang berisi dua fitur: [Age, Interest Score].
- Contoh data latih (Fitur):
  X_train = [ [22, 5.0], [23, 6.0], [45, 8.0], [50, 9.0], [21, 4.0], [48, 7.5] ]
- Contoh label (Kelas: 0 = Tidak Suka, 1 = Suka):
  y_train = [ 0, 0, 1, 1, 0, 1 ]

STEP 2: FUNGSI MENGHITUNG JARAK (EUCLIDEAN DISTANCE)
- Buat fungsi, misalnya `euclidean_distance(point1, point2)`.
- Fungsi ini menerima dua buah list berisikan fitur (contoh: [22, 5.0] dan [25, 8.0]).
- Hitung jarak antara kedua titik tersebut menggunakan rumus Teorema Pythagoras (Akar dari jumlah kuadrat selisih tiap fitur).
- Clue rumus jarak = akar_kuadrat( (x1_a - x2_a)^2 + (x1_b - x2_b)^2 )

STEP 3: FUNGSI MENCARI TETANGGA TERDEKAT (GET NEIGHBORS)
- Buat fungsi, misalnya `get_neighbors(X_train, y_train, test_point, k)`.
- Di dalam fungsi ini:
   a. Buat list kosong, misal `distances`, untuk menyimpan info jarak dan kelas.
   b. Lakukan perulangan untuk setiap baris data di `X_train`.
   c. Hitung jarak dari `test_point` ke data `X_train` saat iterasi berjalan menggunakan fungsi di STEP 2.
   d. Simpan pasangan (jarak, label_kelas) ke dalam list `distances`.
   e. Urutkan list `distances` tersebut berdasarkan jarak dari yang terkecil hingga terbesar (bisa menggunakan `.sort()`).
   f. Ambil sejumlah `k` data teratas (yang jaraknya paling kecil).
- Kembalikan list yang hanya berisi label kelas dari `k` tetangga terdekat tersebut.

STEP 4: FUNGSI VOTING / PREDIKSI KELAS
- Buat fungsi utama, misalnya `predict_classification(X_train, y_train, test_point, k)`.
- Panggil fungsi `get_neighbors` (STEP 3) untuk mendapatkan list kelas tetangga terdekat.
- Hitung jumlah kemunculan (frekuensi) tiap kelas dalam list tersebut (Inilah proses Voting).
- Tentukan kelas mana yang paling banyak muncul (Modus).
- Kembalikan kelas mayoritas tersebut sebagai hasil tebakan/prediksi akhir.

STEP 5: EKSEKUSI & UJI COBA
- Tulis blok pengeksekusian kode di baris paling bawah.
- Tentukan data user baru yang belum ada di dataset latih: `test_user = [25, 8.0]`.
- Tentukan nilai K (jumlah tetangga yang akan dilihat), disarankan angka ganjil agar tidak seri saat voting, misalnya `k = 3`.
- Panggil fungsi `predict_classification` untuk `test_user` tersebut.
- Print hasilnya: "Prediksi untuk user baru adalah kelas: {hasil}"
"""

# MULAI KODING DI BAWAH SINI:


"""
=========================================================
STUDY CASE: THE K-MEANS SEGMENTER
=========================================================
[KETERANGAN SOAL]
K-Means adalah algoritma clustering yang sangat populer untuk segmentasi pelanggan.
Tugas Anda adalah mengelompokkan data pelanggan Mall (Umur & Skor Belanja)
ke dalam K kelompok berdasarkan kemiripan pola mereka, murni dari nol.

[EKSPEKTASI HASIL]
1. Kode dapat menempatkan (assign) setiap titik data ke Centroid terdekat.
2. Kode dapat memindahkan Centroid ke titik rata-rata (mean) dari data anggotanya.
3. Looping berlanjut terus menerus hingga Centroid "berhenti bergerak" (Converge).
4. Hasil akhir bisa divisualisasikan menggunakan utils yang disediakan.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: PERSIAPAN DATASET
- Buat dataset berisi Umur dan Spending Score (berdasarkan dataset_mall_customers.csv atau list).
  Contoh: data = [ [19, 39], [21, 81], [20, 6], [23, 77], ... ]

STEP 2: INISIALISASI CENTROID
- Buat fungsi `initialize_centroids(data, k)`.
- Ambil k data acak (atau k data pertama) dari dataset sebagai Centroid awal.
- Return list berisi koordinat k centroid tersebut.

STEP 3: MENGHITUNG JARAK & CLUSTER ASSIGNMENT
- Buat fungsi `assign_clusters(data, centroids)`.
- Untuk setiap titik data di dalam list 'data':
  a. Hitung jarak (Euclidean) ke semua centroid yang ada.
  b. Cari mana jarak yang paling kecil (terdekat).
  c. Simpan index centroid terdekat sebagai "label" untuk data tersebut.
- Return list `labels` yang ukurannya sama dengan jumlah data.

STEP 4: PEMBARUAN CENTROID (UPDATE)
- Buat fungsi `update_centroids(data, labels, k)`.
- Untuk setiap cluster (dari 0 sampai k-1):
  a. Kumpulkan semua titik data yang memiliki label cluster tersebut.
  b. Hitung rata-rata (mean) untuk fitur X (Umur) dan fitur Y (Spending Score).
  c. Koordinat rata-rata tersebut menjadi Centroid baru.
- Return list `centroids` yang baru.

STEP 5: TRAINING LOOP
- Buat fungsi utama `train_kmeans(data, k, max_iterations=100)`.
- Panggil Step 2 untuk inisialisasi centroid awal.
- Buat perulangan (for/while) maksimal `max_iterations`:
  a. Simpan centroid lama ke dalam variabel sementara (untuk cek kondisi berhenti).
  b. Panggil Step 3 untuk update `labels`.
  c. Panggil Step 4 untuk mendapatkan `centroids` baru.
  d. Cek apakah centroid baru == centroid lama. Jika SAMA PERSIS, hentikan loop (break).
- Return `centroids` akhir dan `labels` akhir.

STEP 6: EKSEKUSI & UJI COBA
- Tulis kode eksekusi di baris paling bawah.
- Tentukan `k = 2` atau `k = 3`.
- Jalankan `train_kmeans`.
- Hitung WCSS menggunakan fungsi `calculate_wcss` dari file `metrics.py`.
- Opsional: Panggil fungsi visualisasi dari `utils_visualization.py` untuk melihat hasil gambarnya!
"""

# MULAI KODING DI BAWAH SINI:


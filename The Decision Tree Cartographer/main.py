"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Ini adalah file pengujian utama untuk mengintegrasikan semua modul
yang telah Anda selesaikan. File ini memuat data, melatih model Decision Tree,
mencetak struktur pohon, dan menguji prediksi pada data baru.

[EKSPEKTASI HASIL]
Menjalankan file ini akan melatih pohon keputusan pada dataset Play Tennis
dan mencetak prediksi untuk beberapa data baru.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: LOAD DATASET
- Panggil `get_dataset()` untuk mengambil data latih, atribut, dan target kelas.

STEP 2: INISIALISASI DAN LATIH MODEL
- Buat objek `DecisionTreeClassifier`.
- Jalankan method `.fit(data, attributes, target_attribute)`.

STEP 3: VISUALISASIKAN POHON
- Gunakan fungsi `print_tree` pada root model (`model.root`) untuk mencetak struktur pohon.

STEP 4: LAKUKAN PREDIKSI PADA DATA UJI BARU
- Tentukan beberapa baris data uji baru, misalnya:
  `test_samples = [{"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "High", "Wind": "Strong"}]`
- Panggil method `.predict(test_samples)` dan cetak hasilnya.
"""

from dataset import get_dataset
from classifier import DecisionTreeClassifier
from utils import print_tree

if __name__ == "__main__":
    # MULAI KODING DI BAWAH SINI:
    pass

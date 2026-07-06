"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Logika utama dari Decision Tree (ID3) adalah memanggil dirinya sendiri
secara rekursif (Recursive Tree Building) untuk membagi data.

[EKSPEKTASI HASIL]
Fungsi `build_tree(data, attributes, target_attribute)` mengembalikan
objek root `Node` yang sudah berisi seluruh struktur cabang pohon keputusan.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: BASE CASES (KRITERIA BERHENTI)
- Kasus A: Jika dataset `data` kosong, kembalikan Leaf Node dengan label None/default.
- Kasus B: Jika semua data memiliki label target yang sama (Entropy = 0),
  kembalikan Leaf Node yang nilainya diisi dengan label target tersebut.
- Kasus C: Jika list `attributes` sudah kosong (tidak ada fitur lagi),
  kembalikan Leaf Node dengan label terbanyak (majority vote) pada dataset saat ini.

STEP 2: PILIH FITUR TERBAIK (BEST SPLIT)
- Cari atribut dari `attributes` yang memiliki nilai Information Gain tertinggi.
- Gunakan fungsi `calculate_information_gain` untuk setiap atribut.
- Atribut dengan Gain tertinggi akan menjadi pembagi di node saat ini.

STEP 3: BUAT NODE KEPUTUSAN BARU
- Buat instansiasi objek `Node` dengan menyimpan atribut terbaik tersebut.

STEP 4: SPLIT DAN REKURSIF CABANG
- Dapatkan semua nilai unik dari atribut terbaik pada dataset saat ini.
- Untuk setiap nilai unik tersebut:
  - Buat subset data menggunakan fungsi `split_dataset`.
  - Buat list atribut baru dengan menghapus atribut terbaik yang telah digunakan.
  - Panggil `build_tree` secara rekursif menggunakan subset data dan list atribut baru.
  - Simpan node anak yang dihasilkan ke dalam dictionary `children` milik node saat ini.

STEP 5: KEMBALIKAN NODE UTAMA
- Kembalikan objek node keputusan yang telah lengkap dengan anak-anak cabangnya.
"""

from node import Node
from info_gain import calculate_information_gain
from splitter import split_dataset

def get_majority_class(data, target_attribute):
    # Helper untuk menghitung kelas terbanyak di data saat ini
    counts = {}
    for row in data:
        val = row[target_attribute]
        counts[val] = counts.get(val, 0) + 1
    return max(counts, key=counts.get) if counts else None

def build_tree(data, attributes, target_attribute):
    # MULAI KODING DI BAWAH SINI:
    pass

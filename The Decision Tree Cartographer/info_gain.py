"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Information Gain (IG) digunakan untuk menentukan seberapa bagus
sebuah atribut untuk membagi data. Atribut dengan IG tertinggi
akan dipilih sebagai pemisah (split) di node tersebut.

[EKSPEKTASI HASIL]
Fungsi `calculate_information_gain(data, attribute, target_attribute)`
mengembalikan float nilai Information Gain.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: HITUNG TOTAL ENTROPY DARI DATA SEBELUM DIBAGI
- Panggil `calculate_entropy(data, target_attribute)` untuk mendapatkan base entropy.

STEP 2: KELOMPOKKAN DATA BERDASARKAN NILAI ATRIBUT
- Pisahkan data ke dalam beberapa subset berdasarkan nilai unik atribut `attribute` yang sedang diuji.

STEP 3: HITUNG RATA-RATA ENTROPY SUBSET (EXPECTED ENTROPY)
- Untuk setiap subset:
  - Hitung bobot subset: (panjang subset) / (total panjang data).
  - Hitung entropy subset tersebut.
  - Jumlahkan hasil perkalian bobot * entropy subset untuk semua subset.

STEP 4: HITUNG INFORMATION GAIN
- Information Gain = Base Entropy - Expected Entropy.
- Return nilai tersebut.
"""

from entropy import calculate_entropy

def calculate_information_gain(data, attribute, target_attribute):
    # MULAI KODING DI BAWAH SINI:
    pass

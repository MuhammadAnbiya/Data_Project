"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Anda diminta untuk menghitung nilai Entropy dari sebuah dataset.
Entropy merepresentasikan ukuran ketidakpastian atau keacakan data.
Nilai entropy tinggi berarti kelas data tercampur, sedangkan nilai
entropy 0 berarti semua data memiliki label kelas yang sama (homogen).

[EKSPEKTASI HASIL]
Fungsi `calculate_entropy(data, target_attribute)` mengembalikan
float nilai entropy sesuai rumus Shannon Entropy.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: HITUNG FREKUENSI KELAS TARGET
- Iterasi seluruh data dalam list, ambil nilai dari `target_attribute`.
- Hitung kemunculan masing-masing label (misal: "Yes" dan "No").

STEP 2: HITUNG PROPORSI/PROBABILITAS (p_i)
- Untuk setiap label unik, bagi jumlah kemunculannya dengan total panjang data.

STEP 3: HITUNG ENTROPY MENGGUNAKAN FORMULA SHANNON
- Gunakan rumus: -sum(p_i * log2(p_i)).
- Gunakan modul `math` bawaan Python.
- Pastikan menangani kondisi jika p_i == 0 agar tidak terjadi math domain error.
"""

import math

def calculate_entropy(data, target_attribute):
    # MULAI KODING DI BAWAH SINI:
    pass

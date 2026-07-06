"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Untuk melakukan split pada node, kita perlu mengambil bagian data
yang memiliki nilai atribut tertentu dan membuang kolom atribut
tersebut agar tidak dievaluasi ulang di level pohon di bawahnya.

[EKSPEKTASI HASIL]
Fungsi `split_dataset(data, attribute, value)` mengembalikan list baru
berisi subset data yang difilter dan kolom `attribute` dihapus dari kamus data.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: FILTER DATA
- Lakukan iterasi pada `data` (list of dicts).
- Ambil baris data yang nilai kunci `attribute`-nya cocok dengan `value`.

STEP 2: HAPUS ATRIBUT YANG SUDAH DIGUNAKAN
- Untuk baris data yang lolos filter, buat dictionary baru (shallow copy).
- Hapus kunci `attribute` dari dictionary baru tersebut.
- Masukkan dictionary baru ke dalam list penampung.

STEP 3: KEMBALIKAN SUBSET
- Return list subset data hasil pemrosesan.
"""

def split_dataset(data, attribute, value):
    # MULAI KODING DI BAWAH SINI:
    pass

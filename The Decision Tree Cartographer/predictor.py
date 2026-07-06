"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Untuk melakukan prediksi pada satu data baru, kita mulai dari root node.
Jika node tersebut bukan leaf node, kita periksa nilai atribut data baru tersebut,
lalu ikuti cabang anak (child node) yang sesuai dengan nilai atribut tersebut.
Proses ini berulang sampai kita menemui leaf node.

[EKSPEKTASI HASIL]
Fungsi `predict_single(node, sample)` mengembalikan label keputusan akhir
berupa string (misal: "Yes" atau "No").

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: CEK APAKAH NODE ADALAH LEAF NODE
- Panggil method `is_leaf()` pada objek `node`.
- Jika mengembalikan `True`, langsung return `node.results` (prediksi selesai).

STEP 2: TEMUKAN NILAI ATRIBUT PADA DATA PENGUJIAN
- Ambil nama atribut dari `node.attribute`.
- Dapatkan nilai atribut tersebut dari dictionary `sample` (data baru yang diuji).

STEP 3: PENELUSURAN CABANG (TRAVERSAL)
- Periksa apakah nilai atribut tersebut ada di dalam dictionary `node.children`.
- Jika ADA, panggil fungsi `predict_single` secara rekursif menggunakan anak node yang cocok dan data `sample` yang sama.
- Jika TIDAK ADA (nilai baru tidak dikenal saat training):
  - Kembalikan keputusan default atau lakukan fallback (misal: return majority class dari subtree ini, atau None).
"""

def predict_single(node, sample):
    # MULAI KODING DI BAWAH SINI:
    pass

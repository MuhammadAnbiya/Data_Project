"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Pohon keputusan dibentuk dari rangkaian node (simpul).
Sebuah node bisa berupa:
1. Node keputusan (Internal Node): Menyimpan nama atribut yang diuji
   dan dictionary berisi anak cabang (child nodes) berdasarkan nilai atribut.
2. Node daun (Leaf Node): Menyimpan label kelas keputusan akhir (misal: "Yes" atau "No").

[EKSPEKTASI HASIL]
Sebuah class `Node` yang dapat merepresentasikan leaf node maupun internal node,
serta mempermudah proses prediksi dan visualisasi pohon.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: METODE __INIT__
- Buat constructor `__init__(self, attribute=None, value=None, results=None)`:
  - `attribute`: Nama atribut yang diuji pada node ini (untuk internal node).
  - `value`: Nilai atribut pemisah yang mengarah ke node ini (opsional).
  - `results`: Label prediksi akhir (untuk leaf node).
  - `children`: Dictionary untuk menampung anak cabang `{nilai_atribut: object_node}`.

STEP 2: CEK APAKAH LEAF NODE
- Buat method `is_leaf(self)`:
  - Return `True` jika `results` tidak bernilai `None`.
  - Return `False` jika sebaliknya.
"""

class Node:
    # MULAI KODING DI BAWAH SINI:
    pass

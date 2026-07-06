"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Untuk mempermudah penggunaan model, kita membungkus logika fit (training)
dan predict (pengujian) ke dalam sebuah class `DecisionTreeClassifier`.

[EKSPEKTASI HASIL]
Class `DecisionTreeClassifier` dengan method `.fit(data, attributes, target_attribute)`
dan `.predict(samples)` yang siap dipakai.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: METHOD INIT
- Constructor kelas menyimpan instance variabel `self.root = None`.

STEP 2: METHOD FIT
- Memanggil fungsi `build_tree` dengan argument `data`, `attributes`, dan `target_attribute`.
- Menyimpan hasil tree root ke dalam `self.root`.

STEP 3: METHOD PREDICT
- Menerima list data uji `samples` (list of dictionaries).
- Melakukan iterasi untuk setiap sample, lalu memanggil fungsi `predict_single` dari root node.
- Mengembalikan list berisi seluruh hasil prediksi.
"""

from builder import build_tree
from predictor import predict_single

class DecisionTreeClassifier:
    # MULAI KODING DI BAWAH SINI:
    pass

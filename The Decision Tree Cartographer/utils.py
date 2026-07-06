"""
=========================================================
STUDY CASE: THE DECISION TREE CARTOGRAPHER
=========================================================
[KETERANGAN SOAL]
Pohon keputusan yang telah dilatih paling mudah dianalisis secara visual.
Tugas Anda adalah menulis fungsi cetak pohon dengan lekukan (indentation)
yang merepresentasikan level kedalaman (depth) cabang pohon.

[EKSPEKTASI HASIL]
Fungsi `print_tree(node, spacing="")` mencetak struktur pohon keputusan ke konsol.

=========================================================
[BLUEPRINT PENGERJAAN - STEP BY STEP]
=========================================================

STEP 1: PERIKSA JIKA LEAF NODE
- Jika `node.is_leaf()` bernilai `True`, cetak spasi lekukan diikuti dengan hasil prediksi `Predict: [results]`.
- Return dari fungsi.

STEP 2: CETAK PERTANYAAN/ATRIBUT NODE SAAT INI
- Cetak spasi lekukan diikuti dengan nama atribut yang diuji `[attribute]`.

STEP 3: REKURSIF CETAK ANAK NODE (CHILDREN)
- Lakukan perulangan untuk setiap nilai cabang `value` dan objek anak `child` di dalam `node.children.items()`:
  - Cetak label cabang: `spacing + '--> Value: ' + str(value)`
  - Panggil `print_tree` secara rekursif untuk node anak tersebut dengan menambahkan spasi tambahan pada spacing (misal: spacing + "    ").
"""

def print_tree(node, spacing=""):
    # MULAI KODING DI BAWAH SINI:
    pass

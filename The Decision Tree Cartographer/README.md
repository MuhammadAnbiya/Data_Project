# The Decision Tree Cartographer

Selamat datang di study case **The Decision Tree Cartographer**! 🌳
Hari ini, kamu akan mempelajari dan membuat salah satu algoritma paling fundamental dan intuitif dalam Machine Learning dari nol menggunakan Python murni: **Decision Tree Classifier** (berbasis algoritma ID3 sederhana).

## Tujuan Pembelajaran
1. Memahami konsep **Entropy** (tingkat ketidakpastian/keacakan data).
2. Memahami konsep **Information Gain** (berapa banyak informasi yang didapat jika kita membagi data berdasarkan suatu atribut).
3. Membangun struktur data Pohon Keputusan (**Tree Node**) menggunakan OOP (Object-Oriented Programming).
4. Mengimplementasikan algoritma rekursif untuk membangun pohon (**Recursive Tree Building**).
5. Melakukan prediksi kelas target berdasarkan keputusan pohon yang telah dibangun.

## Dataset: Play Tennis
Kamu akan menggunakan dataset klasik untuk memprediksi apakah seseorang akan bermain tenis (`Play`) berdasarkan kondisi cuaca (`Outlook`, `Temperature`, `Humidity`, `Wind`).

## Struktur File
Studi kasus ini dipecah secara modular menjadi beberapa berkas blueprint:
- `README.md`: Panduan umum studi kasus.
- `requirements.txt`: Dependensi opsional (misal: matplotlib).
- `hints.txt`: Petunjuk rumus matematika dan tips coding.
- `dataset.py`: Penyedia data latih berupa list of dictionaries.
- `entropy.py`: Penghitung nilai Entropy dataset.
- `info_gain.py`: Penghitung Information Gain dari suatu atribut.
- `node.py`: Representasi node dalam struktur Tree.
- `splitter.py`: Helper untuk memotong/split data.
- `builder.py`: Logika pembangunan pohon secara rekursif.
- `predictor.py`: Logika penelusuran pohon untuk prediksi.
- `classifier.py`: Wrapper utama kelas DecisionTreeClassifier.
- `main.py`: Entry point untuk melatih dan menguji model.

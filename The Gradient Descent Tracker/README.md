# The Gradient Descent Tracker

Selamat datang di study case **The Gradient Descent Tracker**! Hari ini, kamu akan mempelajari dan membuat salah satu algoritma paling fundamental dalam Machine Learning dari nol menggunakan Python murni (tanpa PyTorch, TensorFlow, atau Scikit-Learn).

## 📌 Brief Kasus
Di dunia Machine Learning, **Gradient Descent** adalah algoritma optimasi utama yang digunakan untuk melatih model dengan meminimalkan error. Di sini, kita akan membuat model **Linear Regression** sederhana (sebuah *line fitter*) untuk memprediksi **Gaji (Salary)** berdasarkan **Pengalaman Kerja (Years of Experience)**.

### Dataset:
*   $x$ (Years of Experience): `[1.0, 2.0, 3.0, 4.0, 5.0]`
*   $y$ (Salary - Juta Rupiah): `[5.0, 7.0, 9.0, 11.0, 13.0]` (Secara teoretis, polanya adalah $y = 2x + 3$)

---

## 🛠️ Blueprint & Langkah Pengerjaan

### 1. Model Linear (Hypothesis)
Model kita memprediksi nilai $\hat{y}$ dengan persamaan garis lurus:
$$\hat{y} = w \cdot x + b$$
*   $w$ adalah *weight* (kemiringan garis).
*   $b$ adalah *bias* (titik potong y).

### 2. Cost Function (Mean Squared Error)
Untuk mengukur seberapa buruk/baik tebakan model kita, kita gunakan Mean Squared Error (MSE):
$$L = \frac{1}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)^2$$
*   $N$ adalah jumlah data.
*   $\hat{y}_i$ adalah prediksi ke-$i$.
*   $y_i$ adalah target asli ke-$i$.

### 3. Hitung Gradient (Turunan Parsial)
Arah perubahan $w$ dan $b$ ditentukan dengan menghitung turunan parsial dari Cost Function terhadap masing-masing parameter:
$$\frac{\partial L}{\partial w} = \frac{2}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i) \cdot x_i$$
$$\frac{\partial L}{\partial b} = \frac{2}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)$$

### 4. Parameter Update Rule (Gradient Descent)
Pada setiap iterasi (epoch), perbarui parameter dengan mengurangkan gradient dikalikan dengan *learning rate* ($\alpha$):
$$w = w - \alpha \cdot \frac{\partial L}{\partial w}$$
$$b = b - \alpha \cdot \frac{\partial L}{\partial b}$$

---

## 🚀 Tugas Kamu Hari Ini
Buka file `linear_regression.py` dan lengkapi bagian dengan tanda `# TODO:`:
1.  Lengkapi fungsi `predict(x, w, b)`.
2.  Lengkapi fungsi `compute_cost(y_true, y_pred)`.
3.  Lengkapi fungsi `compute_gradients(x, y_true, y_pred)`.
4.  Lengkapi bagian update parameter di dalam loop training `train()`.
5.  Uji coba model dengan melakukan prediksi pada data pengujian baru ($x = 6.0$).

Setelah selesai, jalankan file Python tersebut dan pastikan cost mendekati `0.0` dan persamaan garis yang dihasilkan mendekati $y = 2x + 3$!

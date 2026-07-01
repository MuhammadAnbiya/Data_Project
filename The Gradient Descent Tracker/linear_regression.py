# The Gradient Descent Tracker
# Sebuah study case untuk mempelajari konsep paling mendasar dari Machine Learning: Gradient Descent & Linear Regression.
# Goal: Mencari garis terbaik (w dan b) untuk memprediksi Gaji berdasarkan Pengalaman Kerja.

# Dataset Dummy:
# x = Years of Experience (Tahun)
# y = Salary (Juta Rupiah)
x_data = [1.0, 2.0, 3.0, 4.0, 5.0]
y_data = [5.0, 7.0, 9.0, 11.0, 13.0] # Hubungan aslinya: y = 2x + 3


# Step 1: Fungsi Prediksi (Hypothesis)
# Menghitung prediksi y_pred untuk sebuah nilai x dengan parameter w dan b saat ini.
def predict(x, w, b):
    # TODO: Kembalikan hasil dari persamaan garis linear (w * x + b)
    pass


# Step 2: Fungsi Cost/Loss (Mean Squared Error)
# Menghitung seberapa jauh prediksi kita dari data yang sebenarnya.
# Rumus MSE: (1 / N) * sum((y_pred - y_true) ^ 2)
def compute_cost(y_true, y_pred):
    # TODO: Hitung Mean Squared Error dari y_true dan y_pred
    pass


# Step 3: Fungsi Gradient (Derivative)
# Menghitung kemiringan (gradient) untuk w dan b agar kita tahu arah pembaruan parameter.
# Rumus dw (turunan terhadap w): (2 / N) * sum((y_pred - y_true) * x)
# Rumus db (turunan terhadap b): (2 / N) * sum(y_pred - y_true)
def compute_gradients(x, y_true, y_pred):
    n = len(x)
    dw = 0
    db = 0
    # TODO: Hitung dw dan db menggunakan loop untuk semua data poin
    return dw, db

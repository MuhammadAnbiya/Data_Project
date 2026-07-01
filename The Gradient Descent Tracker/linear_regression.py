# The Gradient Descent Tracker
# Sebuah study case untuk mempelajari konsep paling mendasar dari Machine Learning: Gradient Descent & Linear Regression.
# Goal: Mencari garis terbaik (w dan b) untuk memprediksi Gaji berdasarkan Pengalaman Kerja.

# Model: y_pred = w * x + b
# Loss: Mean Squared Error (MSE)

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


# Step 4: Gradient Descent (Training Loop)
def train(x, y, epochs, learning_rate):
    # Inisialisasi parameter awal (mulai dari 0)
    w = 0.0
    b = 0.0
    
    print(f"Starting training with learning_rate={learning_rate}...")
    for epoch in range(epochs):
        # 1. Dapatkan prediksi untuk semua data x
        # TODO: Buat list y_pred berisi prediksi untuk setiap elemen di x
        y_pred = []
        
        # 2. Hitung cost/loss saat ini
        # TODO: Hitung cost menggunakan fungsi compute_cost
        cost = 0.0
        
        # 3. Hitung gradient dw dan db
        # TODO: Hitung gradient menggunakan fungsi compute_gradients
        dw, db = 0.0, 0.0
        
        # 4. Update parameter w dan b
        # TODO: Update nilai w dan b berdasarkan gradient dan learning rate
        w = w # lengkapi ini
        b = b # lengkapi ini
        
        # Cetak log setiap 100 epoch untuk melihat penurunan cost
        if epoch % 100 == 0 or epoch == epochs - 1:
            print(f"Epoch {epoch:4d} | Cost: {cost:.6f} | w: {w:.4f} | b: {b:.4f}")
            
    return w, b


# --- EKSEKUSI & UJI COBA ---
if __name__ == "__main__":
    # Hyperparameters
    epochs = 1000
    learning_rate = 0.01
    
    # Jalankan training
    trained_w, trained_b = train(x_data, y_data, epochs, learning_rate)
    
    print("\n--- Training Selesai ---")
    print(f"Hasil Akhir Model: y = {trained_w:.4f} * x + {trained_b:.4f}")
    
    # Step 5: Test Prediksi Data Baru
    # Prediksi gaji untuk orang dengan pengalaman 6 tahun (harusnya mendekati 15.0 juta)
    x_test = 6.0
    # TODO: Gunakan trained_w dan trained_b untuk memprediksi y_test
    # y_test = ...
    # print(f"Prediksi Gaji untuk {x_test} tahun pengalaman: {y_test:.2f} Juta")

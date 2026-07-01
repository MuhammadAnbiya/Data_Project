# Helper Visualization Script
# Script ini digunakan untuk memvisualisasikan data points dan garis linear regression yang diperoleh setelah training.
# Anda baru bisa menjalankan script ini SETELAH Anda menyelesaikan implementasi di 'linear_regression.py'.

import matplotlib.pyplot as plt
import numpy as np

# Import functions from linear_regression.py
try:
    from linear_regression import x_data, y_data, train
except ImportError:
    print("Error: Pastikan file 'linear_regression.py' berada di folder yang sama.")
    exit(1)

# Uji coba training (akan mencetak log ke terminal)
trained_w, trained_b = train(x_data, y_data, epochs=1000, learning_rate=0.01)

# Plotting Data Points asli
plt.scatter(x_data, y_data, color='red', label='Data Asli (Actual Data)')

# Hitung garis regresi hasil training
x_line = np.linspace(min(x_data) - 0.5, max(x_data) + 0.5, 100)
y_line = trained_w * x_line + trained_b

# Plotting Garis Regresi
plt.plot(x_line, y_line, color='blue', label=f'Garis Regresi: y = {trained_w:.2f}x + {trained_b:.2f}')

# Labeling & Styling
plt.title('Visualisasi Linear Regression menggunakan Gradient Descent')
plt.xlabel('Years of Experience (Tahun)')
plt.ylabel('Salary (Juta Rupiah)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Simpan grafik sebagai gambar
plt.savefig('regression_plot.png')
print("Grafik berhasil disimpan sebagai 'regression_plot.png'.")
plt.show()

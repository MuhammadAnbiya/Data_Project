import time

# 1. Setup Data
# Kita gunakan list (seperti kodinganmu sekarang) dan set (untuk optimasi)
positive_list = ["hangat", "bahagia", "spesial", "senang", "cinta", "hebat", "luar biasa", "sukses"]
positive_set = set(positive_list)

# Kita buat input test yang panjang (misal 100.000.000 kata)
test_input = ["hebat"] * 100_000_000

# 2. Benchmark List (Kodinganmu saat ini)
start_list = time.time()
for word in test_input:
    if word in positive_list: # Linear Search: O(N)
        pass
end_list = time.time() - start_list

# 3. Benchmark Set (Optimasi)
start_set = time.time()
for word in test_input:
    if word in positive_set:   # Hash Lookup: O(1)
        pass
end_set = time.time() - start_set

# 4. Hasil
print(f"Waktu pencarian List: {end_list:.6f} detik")
print(f"Waktu pencarian Set  : {end_set:.6f} detik")
print(f"Perbandingan: Set {end_list / end_set:.2f} kali lebih cepat!")
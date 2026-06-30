# Import Library
import math

# User Iteam Matrix
# Baris adalah user, Kolom adalah item dan ada nilai didalamnya rating dari 1-5
# Untuk contoh akan dibuat 5 data dummy

# Challenge: Bagaimana cara merepresentasikan data "user belum menonton film X" (isi dengan 0 atau None).

# Reprensi Data
user_item_matrix = {
    "anbiya": {"pacific rim": 5, "attack on titan": 2, "frierin": 4},
    "nabiel": {"attack on titan": 3, "pacific rim": 1, "fast furious": 5},
    "hazmi": {"fast furious": 4, "attack on titan": 2, "frierin": 2},
    "rendy": {"frierin": 2, "fast furious": 0, "teach u a lesson": 1},
    "rijal": {"teach u a lesson": 0, "attack on titan": 2, "pacific rim": 4}
}

# Tes Output
# print(user_item_matrix["anbiya"])
# print(user_item_matrix["anbiya"]["attack on titan"])


# Data Alignment


# Collect All Movies
# Mengambil semua data Movies yang ditonton user
all_movies = []
for user, inside_dict in user_item_matrix.items():
    for movies in inside_dict.items():
        if movies[0] not in all_movies:
            all_movies.append(movies[0])
# print(all_movies)


# Fungsi Vectorizer
# Mengubah data dictionary menjadi vektor (list angka)
def get_vector(user_name, all_movies):
    vector = []
    
    for movie in all_movies:
        if movie in user_item_matrix[user_name].keys():
            vector.append(user_item_matrix[user_name][movie]) 
        else:   
            vector.append(0)
    return(vector)

print(all_movies)
# print(get_vector("anbiya", all_movies))
# print(get_vector("nabiel", all_movies))

vector_anbiya = get_vector("anbiya", all_movies)
vector_nabiel = get_vector("nabiel", all_movies)

print(vector_anbiya)
print(vector_nabiel)


# Cosine Similarity 3 Step

# Step 1: Fungsi Dot Product (Mengalikan angka di posisi yang sama dari dua vektor, lalu menjumlahkannya.)
def dot_product(vector_a, vector_b):
    sum = 0
    for i in range(len(vector_a)):
        sum += vector_a[i] * vector_b[i]
    return sum

print(dot_product(vector_anbiya, vector_nabiel))


# Step 2: Fungsi Magnitude (Norm)
# Menghutung "Panjang" vektor tersebut
# Akar dari Jumlah Kuadrat setiap elemen didalam vektor
def magnitude(vector):
    sum_of_squares = 0
    for n in vector:
        sum_of_squares += n**2
    return math.sqrt(sum_of_squares)

print(magnitude(vector_anbiya))


# Fungsi Cosice Similarity
# Similarity =  Dot Product(A,B) / Magnitude (A) x Magnitude (B)

def cosine_similarity(vector_a, vector_b):
    result_cs = dot_product(vector_a, vector_b) / (magnitude(vector_a) * magnitude(vector_b))
    return result_cs


print(cosine_similarity(vector_anbiya, vector_nabiel))    


# Tes diri sendiri: Harusnya hasilnya 1.0
print("Similarity anbiya vs anbiya:", cosine_similarity(vector_anbiya, vector_anbiya))

# Tes dengan nabiel:
print("Similarity anbiya vs nabiel:", cosine_similarity(vector_anbiya, vector_nabiel))
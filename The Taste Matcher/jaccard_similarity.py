# Reprensi Data
user_item_matrix = {
    "anbiya": {"pacific rim": 5, "attack on titan": 2, "frierin": 4, "interstellar": 5, "inception": 4},
    "nabiel": {"attack on titan": 3, "pacific rim": 1, "fast furious": 5, "the dark knight": 5, "interstellar": 3},
    "hazmi": {"fast furious": 4, "attack on titan": 2, "frierin": 2, "inception": 5, "john wick": 5},
    "rendy": {"frierin": 2, "fast furious": 0, "teach u a lesson": 1, "parasite": 5, "spirited away": 4},
    "rijal": {"teach u a lesson": 0, "attack on titan": 2, "pacific rim": 4, "john wick": 3, "parasite": 3},
    "sarah": {"frierin": 5, "spirited away": 5, "parasite": 4, "interstellar": 4},
    "fatah": {"john wick": 4, "fast furious": 5, "the dark knight": 5, "pacific rim": 2},
    "budi": {"teach u a lesson": 2, "frierin": 1, "spirited away": 2, "the dark knight": 2}
}

# Step 1: Set Extraction
def get_movies_set(user_name):
    movies_title =set()

    for movies, rating in user_item_matrix[user_name].items():
        if movies not in movies_title:
            movies_title.add(movies)
    return movies_title

print(get_movies_set("anbiya"))


# Step 2: Fase Intersection
# Mencari film yang ada di User A DAN User B.

def get_intersection(set_a, set_b):
    intersection = []
    for movies in set_a:
        if movies in set_b:
            intersection.append(movies)
    
    return len(intersection)


# Step 3: Union 
def get_union(set_a, set_b):
    union = set_a
    for movies in set_b:
        if movies not in union:
            union.add(movies)
    return(len(union))


# Step 4: Jaccard Similarity
intersection_count = get_intersection(get_movies_set("anbiya"), get_movies_set("nabiel"))
union_count = get_union(get_movies_set("anbiya"), get_movies_set("nabiel"))
jaccard_score = intersection_count / union_count

print(jaccard_score)
    

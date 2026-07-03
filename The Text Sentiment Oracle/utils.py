# Helper Functions untuk The Text Sentiment Oracle

def clean_text(text):
    """
    Fungsi ini digunakan untuk membersihkan teks dari tanda baca
    dan mengubahnya menjadi huruf kecil (lowercase).
    
    Cara pakai:
    clean_text("Halo, Dunia!") -> "halo dunia"
    """
    characters_to_remove = [",", ".", "!", "?", "\"", "'", "-", "_"]
    text = text.lower()
    for char in characters_to_remove:
        text = text.replace(char, "")
    return text.strip()

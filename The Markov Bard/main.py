# Markob Bard adalah fondasi LLM seperti ChatGPT terbentuk, dengan menebak kata berikutnya dari sebuah kalimat berdasarkan statistik data yang dilatih

# Step 1: Transition Dictionary (The Brain)
# Ini adalah tempat AI menyimpan "ingatan" tentang bagaimana sebuah kata diikuti oleh kata lainnya.

# aku makan nasi, aku makan bakso
# teks = {
#     "aku": ["makan","makan"],
#     "makan":["nasi","bakso"]
# }


# Aku Makan Nasi. Aku, Makan Bakso
def train_text(text):
    dict_text = {}
    clean_split_text = text.lower().replace(".","").replace(",","").split()

    # DENGAN FOR TEXT IN 
    # i = 0
    # for text in clean_split_text:
    #     if i < len(clean_split_text) - 1:
    #         if text not in dict_text:
    #             dict_text[text] = [clean_split_text[i+1]]
    #         else:
    #             dict_text[text].append(clean_split_text[i+1])
    #     i += 1
    # return dict_text
    
    # DENGAN FOR I IN RANGE
    for i in range(len(clean_split_text) - 1):
        words_now = clean_split_text[i]
        words_after = clean_split_text[i+1]
        if words_now not in dict_text:
            dict_text[words_now] = [words_after]   
        else:
            dict_text[words_now].append(words_after)     
    return dict_text

print(train_text("Aku Makan Nasi. Aku, Makan Bakso"))


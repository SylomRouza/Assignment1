#%%
import nltk
nltk.download('punkt')
data = None
with open('sg_law_cleaned.txt', 'r', encoding='UTF-8') as data_file:
    data = data_file.read()

#%%
output = list(set(nltk.word_tokenize(data)))
output.sort()
# output
# %%
# Stemming TBC

# %%

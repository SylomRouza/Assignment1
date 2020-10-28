from os import listdir
from nltk.stem.snowball import PorterStemmer
from nltk.corpus import stopwords
import nltk
import writer
import re

#nltk.download('stopwords')
stemmer = PorterStemmer()
stopword_list = stopwords.words("english")

def get_tokens_from_sentence(s):
    tokens = nltk.word_tokenize(s.strip())
    final_list = []

    for token in tokens:
        if "//" in token:
            continue

        if re.search("^[+\-\/.].*$", token):
            token = token[1:]

        if not re.search('[a-zA-Z]', token):
            continue

        final_list.append(token)
    return final_list

def get_tokens(data_type):
    folder = "./{0}".format(data_type)
    file_names = [f for f in listdir(folder) if ".txt" in f]
    final_list = []

    for file_name in file_names:
        file = open("{0}/{1}".format(folder, file_name), "r")
        text = file.read()
        lines = text.split("\n")

        for line in lines:
            tokens = nltk.word_tokenize(line.strip())

            for token in tokens:
                token = token.lower()

                if "//" in token:
                    continue

                if re.search("^[+\-\/.].*$", token):
                    token = token[1:]

                if token in stopword_list or not re.search('[a-zA-Z]', token) or re.search("[0-9]$", token):
                    continue

                final_list.append(token)

    final_list = sorted(final_list)
    ret_list = final_list

    data = ""
    final_list = sorted(set(final_list))

    for token in final_list:
        data += "{0}\n".format(token)

    writer.write("Tokens_{0}".format(data_type), data)
    return ret_list

def stem(token_list):
    ret_list = []

    for token in token_list:
        stemmed = stemmer.stem(token)
        ret_list.append(stemmed)

    ret_list = sorted(ret_list)
    return ret_list

def get_token_length_map(token_list):
    token_length_map = {}

    for token in token_list:
        key = str(len(token))

        if key in token_length_map:
            token_length_map[key] += 1
        else:
            token_length_map[key] = 1

    return get_sorted_map(token_length_map)

def get_sentence_length_map(sentence_list):
    length_map = {}

    for sentence in sentence_list:
        word_list = sentence.split(" ")
        key = str(len(word_list))

        if key in length_map:
            length_map[key] += 1
        else:
            length_map[key] = 1

    return get_sorted_map(length_map)

def get_sorted_map(unsorted_map):
    key_list = []

    for key in unsorted_map:
        key_list.append(int(key))

    key_list = sorted(key_list)
    sorted_map = {}

    for key in key_list:
        key = str(key)
        sorted_map[key] = unsorted_map[key]

    return sorted_map

def sentence_segment(data_type):
    folder = "./{0}".format(data_type)
    file_names = [f for f in listdir(folder) if ".txt" in f]
    final_list = []

    for file_name in file_names:
        file = open("{0}/{1}".format(folder, file_name), "r")
        text = file.read()
        tokens = nltk.sent_tokenize(text, "english")

        for token in tokens:
            token = token.replace("\n", " ").strip()
            final_list.append(token)

    return final_list


# token_data["Word Length-Count"] = token_length_list
# token_hist = token_data.hist(column="Word Length-Count")
#
# for ax in token_hist.flatten():
#     ax.set_xlabel("Word Length")
#     ax.set_ylabel("Count")
#
# token_hist

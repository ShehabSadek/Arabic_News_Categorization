import pyarabic.araby as araby
from nltk.stem.isri import ISRIStemmer
from pyarabic.araby import strip_tashkeel
from nltk.corpus import stopwords

def ortho_normalize(text):
    text = araby.normalize_alef(text)
    text = araby.normalize_teh(text)
    return text

def remove_english_text(texts):
    arabic_texts = []
    for text in texts:
        arabic_tokens = [token for token in araby.tokenize(text) if araby.is_arabicrange(token)]
        arabic_text = ' '.join(arabic_tokens)
        arabic_texts.append(arabic_text)
    return arabic_texts

def preprocess_text(texts):
    preprocessed_text = []
    stemmer = ISRIStemmer()
    stop_words = set(stopwords.words('arabic'))

    texts = remove_english_text(texts)

    for text in texts:
        text = araby.strip_tashkeel(text)
        text = ortho_normalize(text)
        tokens = text.split()
        arabic_tokens = [token for token in tokens if araby.is_arabicrange(token)]
        stemmed_tokens = [stemmer.stem(token) for token in arabic_tokens]
        filtered_tokens = [token for token in stemmed_tokens if token not in stop_words and token.isalpha()]
        preprocessed_text.append(' '.join(filtered_tokens))
    
    return preprocessed_text

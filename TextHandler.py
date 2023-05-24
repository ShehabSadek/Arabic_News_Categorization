import pyarabic.araby as araby
from nltk.stem.isri import ISRIStemmer
from pyarabic.araby import strip_tashkeel
from nltk.corpus import stopwords
import re

def remove_english_text(texts):
    arabic_texts = []
    english_pattern = re.compile(r'[a-zA-Z]')
    
    for text in texts:
        arabic_text = re.sub(english_pattern, '', text)
        arabic_texts.append(arabic_text)
    
    return arabic_texts

def preprocess_text(words):
    preprocessed_text = []
    
    stop_words = set(stopwords.words('arabic'))
    
    stemmer = ISRIStemmer()
    words=remove_english_text(words)
    for text in words:
        # Tokenize the text
        tokens = araby.tokenize(text)
        
        # Filter out English words
        arabic_tokens = [token for token in tokens if not token.isascii()]
        
        # Apply stemming and disambiguation
        stemmed_tokens = [stemmer.stem(token) for token in arabic_tokens]
        
        # Filter out stopwords and non-alphabetic tokens
        filtered_tokens = [token for token in stemmed_tokens if token not in stop_words and token.isalpha()]
        
        # Remove diacritics from tokens
        filtered_tokens = [strip_tashkeel(token) for token in filtered_tokens]
        
        # Join the preprocessed tokens
        preprocessed_text.append(' '.join(filtered_tokens))
    
    return preprocessed_text

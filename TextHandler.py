import re
from pyarabic.araby import strip_tashkeel
from pyarabic.araby import tokenize
from nltk.corpus import stopwords

def preprocess_text(words):
    preprocessed_text = []
    
    stop_words = set(stopwords.words('arabic'))
    
    for text in words:
        # Replace variations of 'و' (or) with a space
        text = re.sub(r'\bو\b', ' ', text)
        
        tokens = tokenize(text)
        
        filtered_tokens = [token for token in tokens if token not in stop_words]
        
        filtered_tokens = [token for token in filtered_tokens if token.isalpha()]
        
        filtered_tokens = [strip_tashkeel(token) for token in filtered_tokens]
        
        preprocessed_text.append(' '.join(filtered_tokens))
    
    return preprocessed_text
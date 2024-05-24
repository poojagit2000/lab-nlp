import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
from nltk.corpus import stopwords

def clean_up(s):
    """
    Cleans up numbers, URLs, and special characters from a string.

    Args:
        s: The string to be cleaned up.

    Returns:
        A string that has been cleaned up.
    """
    cleaned_text = re.sub(r'http\S+', '', s)
    cleaned_text = re.sub(r"[^\w\s]",' ', cleaned_text)
    cleaned_text = re.sub(r"\d+", " ", cleaned_text).strip().lower()
    return cleaned_text
text = '''@Ironhack's-#Q website 776-is http://ironhack.com [(2018)]")'''
result = clean_up(text)

def tokenize(s):
    """
    Tokenize a string.

    Args:
        s: String to be tokenized.

    Returns:
        A list of words as the result of tokenization.
    """
    return word_tokenize(s)
tokens = tokenize(result)

def stem_and_lemmatize(l):
    """
    Perform stemming and lemmatization on a list of words.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after being stemmed and lemmatized.
    """
    ps = PorterStemmer()
    lt = WordNetLemmatizer()
    stem_and_lemmatize_words = []
    for word in l:
        stem_word = ps.stem(word)
        lemmatize_word = lt.lemmatize(stem_word)
        stem_and_lemmatize_words.append(lemmatize_word)
    return stem_and_lemmatize_words
text = "Stop Words are the most commonly used words in a language that don't contribute to the main meaning of the texts."    
word_list = text.split()
#print(f"Original Text : {word_list}\n")
result = stem_and_lemmatize(word_list)
#print(f"Stem and lemmatized word : {result}")

def remove_stopwords(l):
    """
    Remove English stopwords from a list of strings.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after stop words are removed.
    """
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in l if word not in stop_words]
    return filtered_words
stop_words_result = remove_stopwords(result)
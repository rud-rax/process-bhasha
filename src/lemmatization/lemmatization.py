import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

NLTK_DATA_PATH = 'var/nltk'

# Download WordNet resources if not already downloaded
nltk.download('wordnet',NLTK_DATA_PATH)
nltk.download('punkt',NLTK_DATA_PATH)
nltk.download('averaged_perceptron_tagger',NLTK_DATA_PATH)

nltk.data.path.append(NLTK_DATA_PATH)

class Lemmatization :

    def __new__(cls) :
        return cls
    
    @classmethod
    def run(cls , lemmatizer , text_data) : 

        lemmatizer = cls.select_lemmatizer(lemmatizer)
        text_processing = TextProcessing()

        # Process the text data
        words = word_tokenize(text_data)

        # Tag each word with its part of speech
        pos_tags = nltk.pos_tag(words)

        # Lemmatize each word using its Part-Of-Speech tag
        lemmatized_words = []
        for word, pos_tag in pos_tags:
            wordnet_pos = text_processing.get_wordnet_pos(pos_tag)
            if wordnet_pos:
                lemma = lemmatizer.lemmatize(word, pos=wordnet_pos)
            else:
                lemma = lemmatizer.lemmatize(word)
            lemmatized_words.append(lemma)

        # Join the lemmatized words back into a single string
        lemmatized_text = ' '.join(lemmatized_words)

        return lemmatized_text
    
    @classmethod
    def select_lemmatizer(cls , lemmatizer_name) :
        if lemmatizer_name == "wordnet" : 
            return WordNetLemmatizer()
    

class TextProcessing :

    def get_wordnet_pos(self,nltk_pos):
        # Map NLTK's POS tags to WordNet's POS tags

        if nltk_pos.startswith('J'):
            return wordnet.ADJ
        elif nltk_pos.startswith('V'):
            return wordnet.VERB
        elif nltk_pos.startswith('N'):
            return wordnet.NOUN
        elif nltk_pos.startswith('R'):
            return wordnet.ADV
        else:
            return None
        
    

if __name__ == "__main__" : 

    l1 = Lemmatization()

    text_data = "Lemmatization is the process of reducing words to their base or dictionary form"


    print("Original Text:")
    print(text_data)
    print("\nLemmatized Text:")
    lemmatized_text = l1.run('wordnet' , text_data)
    print(lemmatized_text)

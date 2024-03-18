from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from abc import ABCMeta , abstractmethod

# Initialize the Porter Stemmer


class Stemming : 

    @staticmethod
    @abstractmethod
    def run(text_data) :

        # Initialize the Porter Stemmer
        porter = PorterStemmer()

        # Tokenize the text into words
        words = word_tokenize(text_data)

        # Perform stemming on each word
        stemmed_words = [porter.stem(word) for word in words]

        # Join the stemmed words back into a single string
        stemmed_text = ' '.join(stemmed_words)

        return stemmed_text



if __name__ == "__main__" : 
        
    text_data = "Stemming is a process of reducing words to their root forms"

    stemmed_text = Stemming.run(text_data)
    print("Original Text:")
    print(text_data)
    print("\nStemmed Text:")
    print(stemmed_text)
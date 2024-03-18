from nltk.stem import PorterStemmer , SnowballStemmer
from nltk.tokenize import word_tokenize


class Stemming : 

    def __new__(cls) :
        return cls

    @classmethod
    def run(cls,stemmer ,text_data) :

        # Initialize the Porter Stemmer
        stemmer = cls.select_stemmer(stemmer)

        # Tokenize the text into words
        words = word_tokenize(text_data)

        # Perform stemming on each word
        stemmed_words = [stemmer.stem(word) for word in words]

        # Join the stemmed words back into a single string
        stemmed_text = ' '.join(stemmed_words)

        return stemmed_text
    

    @classmethod
    def select_stemmer(cls,stemmer_name) :

            if stemmer_name == "porter" : 
                return PorterStemmer()
            if stemmer_name == "snowball" : 
                return SnowballStemmer("english")




if __name__ == "__main__" : 
        
    text_data = "Stemming is a process of reducing words to their root forms"

    stemmed_text = Stemming.run('snowball',text_data)
    print("Original Text:")
    print(text_data)
    print("\nStemmed Text:")
    print(stemmed_text)
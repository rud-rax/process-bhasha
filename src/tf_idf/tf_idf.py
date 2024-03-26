from sklearn.feature_extraction.text import TfidfVectorizer

def tf_idf_vectorizer(documents) : 
    """
        Doc string for 
    """
    
    # Initialize the TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the documents and transform them into TF-IDF vectors
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    # Get the feature names (terms)
    feature_names = tfidf_vectorizer.get_feature_names_out()

    return feature_names , tfidf_matrix


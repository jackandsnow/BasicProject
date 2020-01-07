import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(article_list, n=10):
    """
    extract N keywords from article list through TF-IDF
    :param article_list: list of article str, like ['article1', 'article2', ...]
    :param n: number of keywords, int
    :return: N keywords list
    """
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(article_list)
    words = vectorizer.get_feature_names()
    # check N > total_words_length or not
    maxn = tfidf.shape[1] if tfidf.shape[1] < n else n
    weights = tfidf.toarray()
    # sort by decrease order
    indices = map(lambda w: np.argsort(-w)[:maxn], weights)
    keywords = [list(map(lambda i: words[i], indy)) for indy in indices]
    return keywords

import tarfile
from itertools import islice

def load_yelp_reviews(num_docs):
    f = 'wa_guyup_rukun_sak_lawase_clean.tar'
    with tarfile.open(f) as tar:
            print('Read tar file ... ')
            datafile = tar.extractfile('wa_guyup_rukun_sak_lawase_clean.csv')
            return list(islice(datafile, num_docs))

def make_matrix(docs, binary=False):
    from sklearn.feature_extraction.text import CountVectorizer
    vec = CountVectorizer(min_df=10, max_df=0.1, binary=binary)
    mtx = vec.fit_transform(docs)
    cols = [None] * len(vec.vocabulary_)
    for word, idx in vec.vocabulary_.items():
        cols[idx] = word
    return mtx, cols
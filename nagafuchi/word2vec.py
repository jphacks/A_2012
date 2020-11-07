from gensim.models import KeyedVectors

wv = KeyedVectors.load_word2vec_format('../jawiki.all_vectors.200d.txt', binary=False)
results = wv.most_similar(positive=['アニメ'])
for result in results:
    print(result)


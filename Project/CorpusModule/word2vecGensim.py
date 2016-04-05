import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

# stoplist = set('for a of the and to in considered'.split())
#
# # collect statistics about all tokens
# dictionary = corpora.Dictionary(line.lower().split() for line in open('word2vecdata.txt'))
# # remove stop words and words that appear only once
# stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
#             if stopword in dictionary.token2id]
# once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
# dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
# dictionary.compactify() # remove gaps in id sequence after words that were removed
# print(dictionary)
# dictionary.save('/Users/johnkaufmann/Coding/BME4931/Project/CorpusModule/word2vecdata.dict') # store the dictionary, for future reference

dictionary = corpora.Dictionary.load('/Users/johnkaufmann/Coding/BME4931/Project/CorpusModule/word2vecdata.dict')
corpus = corpora.MmCorpus('/Users/johnkaufmann/Coding/BME4931/Project/CorpusModule/corpus.mm')
tfidf = models.TfidfModel(corpus)

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2) # initialize an LSI transformation
corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi

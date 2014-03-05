import nltk, re, pprint
from nltk import Tree


patterns = """
    NP: {<JJ>*<NN>+}
        {<NNP>+}
        {<NN>+}
    """

NPChunker = nltk.RegexpParser(patterns)


def sentence_parser(input):
    sentences = nltk.sent_tokenize(input)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    sentences = [NPChunker.parse(sent) for sent in sentences]
    nps = []
    for sent in sentences:
        tree = NPChunker.parse(sent)
        for subtree in tree.subtrees():
            if subtree.node == 'NP':
                t = subtree
                t = ' '.join(word for word, tag in t.leaves())
                nps.append(t)
    bigrams = []
    unigrams = []
    space = ' '
    for word in nps:
        if space in word:
            bigrams.append(word)
        else:
            unigrams.append(word)
    fdist1 = FreqDist(word.lower() for word in bigrams)
    fdist2 = FreqDist(word.lower() for word in unigrams)
    vocabulary1 = fdist1.keys()
    vocabulary2 = fdist2.keys()
    return vocabulary1[:5], vocabulary2[:5]


    # for tree in nps:
    #     t = tree
    #     t = t.leaves()
    #     t = ''.join(word for word, tag in t.leaves())
    #     nps_new.append(t)
    # return nps_new
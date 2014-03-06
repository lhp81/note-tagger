import nltk
# import re
# import pprint
from nltk import Tree
import tech_list
import music_list


patterns = """
    NP: {<JJ>*<NN>+}
        {<NNP>+}
        {<NN>+}
    """

NPChunker = nltk.RegexpParser(patterns)

def prepare_text(input):
    patterns = """
    NP: {<JJ>*<NN>+}
        {<NNP>+}
        {<NN>+}
    """
    NPChunker = nltk.RegexpParser(patterns)
    sentences = nltk.sent_tokenize(input)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    sentences = [NPChunker.parse(sent) for sent in sentences]
    return sentences


def parsed_text_to_NP(sentences):

    nps = []
    for sent in sentences:
        tree = NPChunker.parse(sent)
        for subtree in tree.subtrees():
            if subtree.node == 'NP':
                t = subtree
                t = ' '.join(word for word, tag in t.leaves())
                nps.append(t)
# I think the following is unnecessary since we don't want a list of
# keywords from the input. We can skip this, maybe, and instead just go
# right into the checking NP against category keywords.
# bigrams, unigrams, space = [], [], ' '
# for word in nps:
#     if space in word:
#         bigrams.append(word)
#     else:
#         unigrams.append(word)
# fdist1 = nltk.FreqDist(word.lower() for word in bigrams)
# fdist2 = nltk.FreqDist(word.lower() for word in unigrams)
# vocabulary1, vocabulary2 = fdist1.keys(), fdist2.keys()


def category_chooser(sentences):
    tech_counter = 0
    music_counter = 0
    for word in nps:
        if word in tech_list:
            tech_counter += 1
        if word in music_list:
            music_counter += 1
    category_tag = None
    if tech_counter > music_counter:
        category_tag = 'Technology'
    else:
        category_tag = 'Music'
    return [category_tag]

import nltk
import re
import pprint
from nltk import Tree
from tech_list import tech_list
from music_list import music_list


patterns = """
    NP: {<JJ>*<NN>+}
        {<NNP>+}
        {<NN>+}
        {<NN*>+}
    """

NPChunker = nltk.RegexpParser(patterns)

def prepare_text(input):
    """Returns sentences that are POS tagged for NP using re.
    The steps are:
    (a) defines patterns of text that are NP
    (b) defines a parser that will look for those patterns
    (c) breaks the text into sentences and individual words.
    (d) tags each word for its part of speech
    (e) uses my regexs and parser to label NP.
    """
    sentences = nltk.sent_tokenize(input)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    sentences = [NPChunker.parse(sent) for sent in sentences]
    return sentences


def parsed_text_to_NP(sentences):
    """ Returns a list of noun phrases.
    Takes parsed sentences from prepare_text and extracts only the NP.
    These NP are stripped of POS tags and stored in a list.
    """
    nps = []
    for sent in sentences:
        tree = NPChunker.parse(sent)
        for subtree in tree.subtrees():
            if subtree.node == 'NP':
                t = subtree
                t = ' '.join(word for word, tag in t.leaves())
                nps.append(t)
    return nps
    # I think the following is unnecessary since we don't want a list of
    # keywords from the input. We can skip this, maybe, and instead just go
    # right into the checking NP against category keywords.
    # 
    # bigrams, unigrams, space = [], [], ' '
    # for word in nps:
    #     if space in word:
    #         bigrams.append(word)
    #     else:
    #         unigrams.append(word)
    # fdist1 = nltk.FreqDist(word.lower() for word in bigrams)
    # fdist2 = nltk.FreqDist(word.lower() for word in unigrams)
    # vocabulary1, vocabulary2 = fdist1.keys(), fdist2.keys()


def category_chooser(nps):
    """ Returns a category tag based upon NPs extracted above.
    Goes through the list of NP, comparing each NP to
        category lists of keywords. This is done to determine which of the
        category tags should be appended.
    """
    tech_counter = 0
    music_counter = 0
    for word in nps:
        if word.lower() in tech_list:
            tech_counter += 1
        if word.lower() in music_list:
            music_counter += 1
    category_tag = None
    if tech_counter > music_counter:
        category_tag = 'Technology'
    elif (tech_counter == music_counter) and tech_counter != 0:
        category_tag = ('Music', 'Technology')
    elif tech_counter < music_counter:
        category_tag = 'Music'
    else:
        category_tag = ("Unable to find appropriate category. Please suggest "
                        "your own and resubmit.")
    return [category_tag]


def sent_parse(input):
    sentences = prepare_text(input)
    nps = parsed_text_to_NP(sentences)
    category_tag = category_chooser(nps)
    return category_tag

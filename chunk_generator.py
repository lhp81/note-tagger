import nltk, re, pprint


"""
About:
===================
ongoing work on our chunk generator. this is something that will go through a
text and find the most common noun phrases. the idea behind this is that noun
phrases that occur with higher frequency will probably be important and reflect
what the note is about.
this is something to be extended; probably we would want to implement a related
words search or something like that on the most common words, seeing if that
will help to bring up more general keywords.

The below was inspired by:
Zhu, D. "Text Chunking using NLTK". Online at:
    http://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf
The NLTK Book. Online at: http://nltk.org/book
"""


"""
Plan of attack:
===================
First: Segment, tokenize, and tag, using the NLTK's resources.
Second: Chunk using the predetermined patterns.
Third: Return the most common chunks.
Fourth: Profit. Failing that, find a prophet to follow. First choice > second.
"""


# to-dos:
# 3. store NP chunks
# 4. extract keywords based upon frequency


"""First: Segment, tokenize, and tag, using the NLTK's resources."""

# wrapped up in the below.

"""Second: Chunk using predetermined patterns"""

# set the patterns we want to look for
patterns = """
    NP: {<JJ>*<NN>+}
    {<JJ>*<NN*>?<NN>+}
    {<NNP>+<NNPS>+}
    {<NN>+<NNS>+}
    {<NN>?<NNP>*<CD>}
    {<NNP>+<NN>+}
    {<NN>+<NN>+}
    {<NNP>+<CD>+}
    """
    # {<NNP>+}
    # {<NN>+}

# the above needs to be extended after I can see real world results
# may want to start using <NN*> as a choice.

# create a chunk parser that works using the above patterns.
NPChunker = nltk.RegexpParser(patterns)


# this will parse the sentences, starting our NP identification process.
def sentence_parser(input):
    results = []
    sentences = nltk.sent_tokenize(input)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    for sent in sentences:
        result = NPChunker.parse(sent)
        results.append(result)


"""Third: Return the most common chunks."""

# a tree traversal function for extracting NP chunks in the parsed tree
# so this will go through the results from sentence_parser and just pick out
# the NP.


def traverse(t):
    cool_nps = []
    try:
        t.node
    except AttributeError:
        return
    else:
        if t.node == 'NP':
            cool_nps.append(t)  # or do whatever else...think abt it. -lp
        else:
            for child in t:
                traverse(child)
    return cool_nps

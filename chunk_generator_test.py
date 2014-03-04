import nltk, re, unittest
from chunk_generator import *


class ChunkGeneratorConstituentsTest(unittest.TestCase):
    """ testing the various parts of the chunker"""

    def test_sentence_parser(self):
        sentences = "Four score and seven years ago, our fathers brought \
            upon this continent a new nation, conceived in liberty \
            and dedicated to the proposition that all men are created \
            equal. Now we are engaged in a great civil war, testing \
            whether that nation, or any nation so conceived and so \
            dedicated, can long endure."
        sentences = nltk.sent_tokenize(sentences)
        self.assertEqual(len(sentences), 2)

    def test_sentence_tagger(self):
        sentences = "Four score and seven years ago, our fathers brought \
            upon this continent a new nation, conceived in liberty \
            and dedicated to the proposition that all men are created \
            equal. Now we are engaged in a great civil war, testing \
            whether that nation, or any nation so conceived and so \
            dedicated, can long endure."
        sentences = nltk.sent_tokenize(sentences)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        self.assertEqual(len(sentences[0]), 32)
        # this is 32 because there are 32 distinct items in the first sentence,
        # where items are words and pieces of punctuation.
        # sent_tokenize creates two lists, word_tokenize breaks sentences up
        # into words.

    def test_word_tagger(self):
        sentences = "Four score and seven years ago, our fathers brought \
            upon this continent a new nation, conceived in liberty \
            and dedicated to the proposition that all men are created \
            equal. Now we are engaged in a great civil war, testing \
            whether that nation, or any nation so conceived and so \
            dedicated, can long endure."
        sentences = nltk.sent_tokenize(sentences)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        self.assertEqual(sentences[0][1], ('score', 'NN'))
        # check that the second word of the address, 'score' is correctly
        # tagged as a noun. Different taggers were doing different things with
        # the word 'four'...so I went with something safe.



if __name__ == '__main__':
    unittest.main()
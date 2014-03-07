import nltk, re, unittest
from note_tagger_app import *


SENTENCES = """Four score and seven years ago, our fathers brought
            upon this continent a new nation, conceived in liberty
            and dedicated to the proposition that all men are created
            equal. Now we are engaged in a great civil war, testing
            whether that nation, or any nation so conceived and so
            dedicated, can long endure."""

TECH_SENTENCES = """If I were to buy something that I really want, it would
                be an iPhone 5. I like Apple because the App Store offers more
                apps than the Google Play Store. I think that Android is a good
                operating system, but from my experience, iOS is just more
                reliable. I like that you don't have to jailbreak Android,
                but reliability, and the timet that it saves me, trumps the
                ability to customize."""

MUSIC_SENTENCES = """When I got back to Beijing from Scotland, my wife
                    surprised me with tickets to an opera. I love classical
                    music, going to the symphony, everything like that, so it
                    was a good gift to give me. We heard a recital by the
                    Korean opera singer Sumi Jo, who is fantastically talented.
                    """



class ChunkGeneratorConstituentsTest(unittest.TestCase):
    """ testing the various parts of the chunker"""

    def test_sentence_parser(self):
        sentences = nltk.sent_tokenize(SENTENCES)
        self.assertEqual(len(sentences), 2)

    def test_sentence_tagger(self):
        sentences = nltk.sent_tokenize(SENTENCES)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        self.assertEqual(len(sentences[0]), 32)
        # this is 32 because there are 32 distinct items in the first sentence,
        # where items are words and pieces of punctuation.
        # sent_tokenize creates two lists, word_tokenize breaks sentences up
        # into words.

    def test_word_tagger(self):
        sentences = nltk.sent_tokenize(SENTENCES)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        self.assertEqual(sentences[0][1], ('score', 'NN'))
        # check that the second word of the address, 'score' is correctly
        # tagged as a noun. Different taggers were doing different things with
        # the word 'four'...so I went with something safe.

class TestConstituentParts(unittest.TestCase):
    """testing the functions within my note_tagger_app script."""

    def test_untaggable_text(self):
        sentences = sent_parse(SENTENCES)
        self.assertEqual(sentences, (["Unable to find appropriate category. "
            "Please suggest your own and resubmit."]))

    def test_tech_sentences(self):
        sentences = sent_parse(TECH_SENTENCES)
        self.assertEqual(sentences, ['Technology'])

    def test_music_sentences(self):
        sentences = sent_parse(MUSIC_SENTENCES)
        self.assertEqual(sentences, ['Music'])


if __name__ == '__main__':
    unittest.main()

import nltk, re, pprint
from nltk import Tree


patterns = """
    NP: {<JJ>*<NN>+}
        {<NNP>+}
        {<NN>+}
    """

NPChunker = nltk.RegexpParser(patterns)

tech_list = ['3d Crystal Engraving', '3d Digitizer', '3d Glass Buy', '3d Laser Scanner', '3d Led Tv', '3d Plastic Printer', '3d Printer', '3d Printer kit', '3d Printer price', '3d Projector', '3d Satellite Maps', '3d Scan', '3d Scanner', '3d Scanning', '3d Tv', '3ds Games', '3g Dongle', '3g Router', '3g Tablet', '4', 'Aaron Swartz', 'Acta', 'Adobe', 'Advanced Robotics', 'AI', 'Amazon', 'Android', 'Android App', 'Android Apps free', 'Android Phones', 'Angry Bird', 'Anonymous VPN', 'App Android', 'App Creator', 'App Development', 'App Maker', 'App Store', 'Apple Ipad', 'Apple Ipad 2', 'Apps', 'Arpanet', 'Artificial Intelligence', 'Audiable', 'Audio Book', 'Augmented Reality', 'Bandwidth', 'Bebo', 'Big Data', 'Bill Gates', 'Bing', 'Bitcoin', 'Bitcoin Exchange', 'Bit-torrent', 'Blackberry', 'Blogging', 'Blu-Ray', 'Broadband', 'Browse Anonymously', 'Buy 3d Printer', 'Carol Bartz', 'Ces 2013', 'Chat Groups', 'Cheap Android Tablets', 'Cheap Ipad', 'Cheap Wireless Internet', 'Cheapest Android Phones', 'Chrome', 'Computer Games', 'Computer Science', 'Computer Security', 'Create Android Apps', 'Data Card', 'Desktop 3d Printer', 'EA Games', 'Ebook', 'Ebook Reader', 'Electronic Book', 'Email Providers', 'Emule', 'Expert System', 'Facebook', 'Free Apps', 'Free Arcade', 'Free Ebooks', 'Free Email Accounts', 'Free Games', 'Free Games To Play', 'Free Online Books', 'Free Online Virtual Games', 'Free Pdf Reader', 'Free Voip Calls', 'Freelance Writing', 'Frogger', 'Galaga', 'Games Online', 'Gmail', 'Hi5', 'High speed Internet Providers', 'Hologram Printing', 'Hotmail', 'HTC Evo', 'Instant Messenger', 'Ipad', 'Ipad 2 Cover', 'Keri Allan', 'Laser 3d Scanner', 'Lenticular Printing', 'Linkedin', 'Mobile Apps', 'Moblie Phones', 'Modem 3g', 'Monster.com', 'Myspace', 'Neural Network', 'Nintedo', 'Online Books', 'Online Privacy act', 'Online Publications', 'Online Shopping', 'Pc Games Free', 'Pdf Converter Software', 'Photo Editor', 'Photoshop', 'Play Games', 'Proxy Server', 'Rapid Prototype Machine', 'Robot', 'Robotics', 'Robotics Application', 'Robotics Engineering', 'Routers', 'Satellite Internet', 'Spiele', 'Stev Jobes', 'Stock Market', 'Tablet', 'Tablet Pc', 'Twitter', 'Usb Internet', 'Video Hosting', 'Virtual Reality', 'Vodafone', 'Webcam', 'Wifi Routers', 'Wikipedia', 'Windows', 'Windows Vps', 'Wireless Broadband', 'Wireless Internet', 'World Wide Web', 'X Box Price', 'Yahoo', 'Youtube', 'Youtube Games', 'Zynga']

def sent_parse(input):
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
    bigrams, unigrams, space = [], [], ' '
    space = ' '
    for word in nps:
        if space in word:
            bigrams.append(word)
        else:
            unigrams.append(word)
    fdist1 = FreqDist(word.lower() for word in bigrams)
    fdist2 = FreqDist(word.lower() for word in unigrams)
    vocabulary1, vocabulary2 = fdist1.keys(), fdist2.keys()
    tech_counter = 0
    tech_words_from_txt = []
    for word in nps:
        if word in new_list:
            tech_counter += 1
            tech_words_from_txt.append(word)
    return tech_counter, tech_words_from_txt
    # return vocabulary1[:5], vocabulary2[:5]


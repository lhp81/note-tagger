import nltk, re, pprint
from nltk import Tree


patterns = """
    NP: {<JJ>*<NN>+}
        {<NNP>+}
        {<NN>+}
    """

NPChunker = nltk.RegexpParser(patterns)

tech_list = ['3d Crystal Engraving', '3d Digitizer', '3d Glass Buy', '3d Laser Scanner', '3d Led Tv', '3d Plastic Printer', '3d Printer', '3d Printer kit', '3d Printer price', '3d Projector', '3d Satellite Maps', '3d Scan', '3d Scanner', '3d Scanning', '3d Tv', '3ds Games', '3g Dongle', '3g Router', '3g Tablet', '4', 'Aaron Swartz', 'Acta', 'Adobe', 'Advanced Robotics', 'AI', 'Amazon', 'Android', 'Android App', 'Android Apps free', 'Android Phones', 'Angry Bird', 'Anonymous VPN', 'App Android', 'App Creator', 'App Development', 'App Maker', 'App Store', 'Apple Ipad', 'Apple Ipad 2', 'Apps', 'Arpanet', 'Artificial Intelligence', 'Audiable', 'Audio Book', 'Augmented Reality', 'Bandwidth', 'Bebo', 'Big Data', 'Bill Gates', 'Bing', 'Bitcoin', 'Bitcoin Exchange', 'Bit-torrent', 'Blackberry', 'Blogging', 'Blu-Ray', 'Broadband', 'Browse Anonymously', 'Buy 3d Printer', 'Carol Bartz', 'Ces 2013', 'Chat Groups', 'Cheap Android Tablets', 'Cheap Ipad', 'Cheap Wireless Internet', 'Cheapest Android Phones', 'Chrome', 'Computer Games', 'Computer Science', 'Computer Security', 'Create Android Apps', 'Data Card', 'Desktop 3d Printer', 'EA Games', 'Ebook', 'Ebook Reader', 'Electronic Book', 'Email Providers', 'Emule', 'Expert System', 'Facebook', 'Free Apps', 'Free Arcade', 'Free Ebooks', 'Free Email Accounts', 'Free Games', 'Free Games To Play', 'Free Online Books', 'Free Online Virtual Games', 'Free Pdf Reader', 'Free Voip Calls', 'Freelance Writing', 'Frogger', 'Galaga', 'Games Online', 'Gmail', 'Google', 'Hi5', 'High speed Internet Providers', 'Hologram Printing', 'Hotmail', 'HTC Evo', 'Instant Messenger', 'Ipad', 'Ipad 2 Cover', 'Keri Allan', 'kindle', 'Laser 3d Scanner', 'Lenticular Printing', 'Linkedin', 'Mobile Apps', 'Moblie Phones', 'Modem 3g', 'Monster.com', 'Myspace', 'Neural Network', 'Nintedo', 'Online Books', 'Online Privacy act', 'Online Publications', 'Online Shopping', 'Pc Games Free', 'Pdf Converter Software', 'Photo Editor', 'Photoshop', 'Play Games', 'Proxy Server', 'Rapid Prototype Machine', 'Robot', 'Robotics', 'Robotics Application', 'Robotics Engineering', 'Routers', 'Samsung', 'Satellite Internet', 'Spiele', 'Stev Jobes', 'Stock Market', 'Tablet', 'Tablet Pc', 'Twitter', 'Usb Internet', 'Video Hosting', 'Virtual Reality', 'Vodafone', 'Webcam', 'Wifi Routers', 'Wikipedia', 'Windows', 'Windows Vps', 'Wireless Broadband', 'Wireless Internet', 'World Wide Web', 'X Box Price', 'Yahoo', 'Youtube', 'Youtube Games', 'Zynga']

music_list = ['A cappella', 'Accelerando', 'Accessible', 'Adagio', 'Allegro', 'Atonal', 'Baroque', 'Beat', 'Cadence', 'Cadenza', 'Cadenza', 'Canon', 'Cantabile', 'Cantata', 'Capriccio', 'Carol', 'Castrato', 'Cavatina', 'Chamber music', 'Chant', 'Choir', 'Chorale', 'Chord', 'Chord progression', 'Chorus', 'Chromatic scale', 'Classical', 'Classicism', 'Clavier', 'Clef', 'Coda', 'Concert master', 'Concerto', 'Conductor', 'Consonance', 'Contralto', 'Counterpoint', 'Courante', 'Da Capo', 'Deceptive cadence', 'Development', 'Dissonance', 'Drone', 'Duet', 'Dynamics', 'Elegy', 'Encore', 'Energico', 'Enharmonic Interval', 'Ensemble', 'Espressivo', 'Etude', 'Exposition', 'Expressionism', 'Falsetto', 'Fermata', 'Fifth', 'Finale', 'Flat', 'Form', 'Forte', 'Fourth', 'Fugue', 'Galliard', 'Gavotte', 'Glee', 'Glissando', 'Grandioso', 'Grave', 'Grazioso', 'Gregorian Chant', 'Harmony', 'Homophony', 'Hymn', 'Impromptu', 'Instrumentation', 'Interlude', 'Intermezzo', 'Interpretation', 'Interval', 'Intonation', 'Introduction', 'Key', 'Key signature', 'Klangfarbenmelodie', 'Leading note', 'Legato', 'Leitmotif', 'Libretto', 'Ligature', 'Madrigal', 'Maestro', 'Major', 'March', 'Measure', 'Medley', 'Mezzo', 'Minor', 'Minuet', 'Modes', 'Modulation', 'Monotone', 'Motif', 'Movement', 'Musette', 'Musicology', 'Natural', 'Neoclassical', 'Nocturne', 'Nonet', 'Notation', 'Obbligato', 'Octave', 'Octet', 'Opera', 'Operetta', 'Opus', 'Oratorio', 'Orchestra', 'Orchestration', 'Ornaments', 'Ostinato', 'Overture', 'Parody', 'Part', 'Partial', 'Partita', 'Pastoral', 'Pentatonic Scale', 'Phrase', 'Piano', 'Pitch', 'Pizzicato', 'Polyphony', 'Polytonality', 'Portamento', 'Prelude', 'Presto', 'Progression', 'Quadrille', 'Quartet', 'Quintet', 'Recapitulation', 'Recital', 'Recitative', 'Reed', 'Refrain', 'Register', 'Relative major and minor', 'Relative pitch', 'Renaissance', 'Reprise', 'Requiem', 'Resonance', 'Rhythm', 'Ricercar', 'Rigaudon', 'Rococo', 'Romantic', 'Rondo', 'Root', 'Round', 'Rubato', 'Scale', 'Scherzo', 'Scordatura', 'Septet', 'Sequence', 'Serenade', 'Sextet', 'Sharp', 'Slide', 'Slur', 'Sonata', 'Sonata form', 'Sonatina', 'Song cycle', 'Soprano', 'Staccato', 'Staff', 'Stretto', 'String Quartet', 'Suite', 'Symphony', 'System', 'Tablature', 'Temperament', 'Tempo', 'Tessitura', 'Theme', 'Timbre', 'Time Signature', 'Tonal', 'Tonality', 'Tone', 'Tone less', 'Tonic', 'Treble', 'Tremolo', 'Triad', 'Trill', 'Trio', 'Triple time', 'Triplet', 'Tritone', 'Tune', 'Tuning', 'Tutti', 'Twelve-tone music', 'Unison', 'Verismo', 'Vibrato', 'Virtuoso', 'Vivace', 'Voice', 'Waltz', 'Whole note', 'Whole-tone scale']

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
    music_counter = 0
    for word in nps:
        if word in tech_list:
            tech_counter += 1
    # for word in nps:
    #     if word in music_list:
    #         music_counter += 1
    category_tag = None
    if tech_counter > music_counter:
        category_tag = 'Technology'
    else:
        category_tag = 'Music'
    return [category_tag, (vocabulary1[:3], vocabulary2[:3])]
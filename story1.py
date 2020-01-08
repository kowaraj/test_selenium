story_dict = {
    'a'       : 'une',
    'a lot'   : 'beaucoup',
    'am'      : 'suis',
    'are'     : 'es',
    'at'      : 'à',
    'at home' : 'à la maison',
    'book'    : 'livre',
    'cup'     : 'tasse',
    'coffee'  : 'café',
    'darling' : 'chéri',
    'drinks'  : 'boit',
    'English test' : 'examen d\'anglais',
    'English book' : 'livre d\'anglais',
    'good morning' : 'Bonjour !',
    'here it is'   : 'Voilà',
    'here'    : 'ici',
    'hi'      : 'Salut',
    'his'     : 'sa',
    'her'     : 'son',
    'I'       : 'Je',
    'I have'  : 'J\'ai',
    'it\'s'   : 'C\'est',
    'in'      : 'dans',
    'is'      : 'est',
    'it'      : 'Il',
    'of'      : 'de',
    'on'      : 'sur',
    'puts'    : 'met',
    'my'      : 'mon', 
    'some sugar' : 'du sucre',
    'some salt'  : 'du sel',
    'she'     : 'Elle',
    'sorry'   : 'Pardon',
    'table'   : 'table', 
    'thank you': 'merci',
    'the'     : 'la', 
    'the university': 'l\'université',
    'tired'   : 'fatiguée', 
    'very'    : 'très',
    'want'    : 'veux',
    'where'   : 'Où',
    'what'    : 'Quoi',
    'with'    : 'avec',
    'women,wife': 'femme',
    'work'    : 'travaille',
    'yes'     : 'Oui',
    'yuck'    : 'Beurk',
    'you'     : 'Tu'


}

class StoryDict(dict): 

    def __init__(self):
        super().__init__(story_dict)

    def __missing__(self, key):

        for k in self.keys():
            # Handle many-to-one case, like "wife,woman -> femme"
            if key in k.split(','):
                return self[k]

            # Handle the reverse look-up (from french to english)
            val = self[k]
            if key == val:
                print('Key not found. Found a value: ' + val + ' of k = ' + k)
                return k

        # Handle the unknown token
        val = input('Enter a value for : ' + key + ' <--- ')
        self[key] = val
        self[val] = key
        return val







# def expand_dict(d_in):
#     d = d_in.copy()
#     for k in d_in.keys():
#         v = d_in[k]
#         d[v] = k
#     return d

dict = {
    'a'       : 'une',
    'a lot'   : 'beaucoup',
    'are'     : 'es',
    'at'      : 'à',
    'at home' : 'à la maison',
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
    'where'   : 'Où',
    'what'    : 'Quoi',
    'with'    : 'avec',
    'women'   : 'femme',
    'work'    : 'travaille',
    'yes'     : 'Oui',
    'yuck'    : 'Beurk'


}

def expand_dict(d_in):
    d = d_in.copy()
    for k in d_in.keys():
        v = d_in[k]
        d[v] = k
    return d

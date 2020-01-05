dict = {
    'a lot'   : 'beaucoup',
    'are'     : 'es',
    'at'      : 'à',
    'cup'     : 'tasse',
    'darling' : 'chéri',
    'drinks'  : 'boit',
    'good morning' : 'Bonjour !',
    'here'    : 'ici',
    'hi'      : 'Salut',
    'his'     : 'sa',
    'I'       : 'Je',
    'I have'  : 'J\'ai',
    'it\'s'   : 'C\'est',
    'in'      : 'dans',
    'is'      : 'est',
    'of'      : 'de',
    'on'      : 'sur',
    'puts'    : 'met',
    'my'      : 'mon', 
    'some sugar' : 'du sucre',
    'she'     : 'Elle',
    'sorry'   : 'Pardon',
    'table'   : 'table', 
    'tired'   : 'fatiguée', 
    'where'   : 'Où',
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

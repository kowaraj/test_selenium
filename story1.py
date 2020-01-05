dict = {
    'a lot'   : 'beaucoup',
    'are'     : 'es',
    'table'   : 'table', 
    'puts'    : 'met',
    'where'   : 'Où',
    'it\'s'   : 'C\'est',
    'in'      : 'dans',
    'drinks'  : 'boit',
    'of'      : 'de',
    'on'      : 'sur',
    'my'      : 'mon', 
    'some sugar' : 'du sucre',
    'she'     : 'Elle',
    'his'     : 'sa',
    'darling' : 'chéri',
    'I'       : 'Je',
    'I have'  : 'J\'ai',
    'yuck'    : 'Beurk',
    'good morning' : 'Bonjour !',
    'sorry'   : 'Pardon',
    'work'    : 'travaille',
    'cup'     : 'tasse',
    'women'   : 'femme',
    'tired'   : 'fatiguée', 
    'yes'     : 'Oui'


}

def expand_dict(d_in):
    d = d_in.copy()
    for k in d_in.keys():
        v = d_in[k]
        d[v] = k
    return d

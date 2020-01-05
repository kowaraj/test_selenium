dict = {
    'women'   : 'femme',
    'tired'   : 'fatiguée', 
    'a lot'   : 'beaucoup',
    'table'   : 'table', 
    'puts'    : 'met',
    'where'   : 'Où',
    'are'     : 'es',
    'it\'s'   : 'C\'est',
    'in'      : 'dans',
    'drinks'  : 'boit',
    'of'      : 'de',
    'my'      : 'mon', 
    'some sugar' : 'du sucre',
    'she'     : 'Elle',
    'darling' : 'chéri'

}

def expand_dict(d_in):
    d = d_in.copy()
    for k in d_in.keys():
        v = d_in[k]
        d[v] = k
    return d

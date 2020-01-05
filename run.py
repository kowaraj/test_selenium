import duolingo

a1 = 'My darling.'
a2 = 'examen d\'anglais'
a3 = 'She put sugar in her cup of coffee.'
a4 = 'What?'
a5 = '… put salt in her coffee instead of sugar.'

def run():
    d = duolingo.Duolingo('Chrome')
    d.click_alread_have_an_account()
    d.provide_credentials()
    d.click_login()
    d.switch_to_stories()

    d.start_the_story() 

    d.click_continue(1) # bonjour
    d.click_continue(4) # jean est a la maison avec ca femme marion
    d.click_continue(2) # salut marion
    d.click_continue(3) # salut mon cheri
    d.click_continue( ) # .

    d.pick_li_answer(a1) # My darling
    #d.pick_my_darling()

    d.click_continue(3) # ou est mon livre d'anglais
    d.click_continue(2) # pardon
    d.click_continue(4) # j'ai un examen d'anglais a l'univerite

    d.pick_li_answer(a2) # examen d'anglais

    d.click_continue( ) # . 
    d.click_continue(3) # ou est mon livre
    d.click_continue(4) # il est ici,.. sur la table,.. marion + click
    d.click_continue(3) # (3sec for:)je suis fatiguee jean, je travail beaucoup (+ click)

    d.pick_6th_phrase() # fatigueeee
    d.click_continue( ) # . 
    d.click_continue(3) # tu veux une tasse du cafee?
    d.click_continue(2) # oui, merci
    d.click_continue(2) # voila
    d.click_continue(3) # marion mets du sucre dans ca tasse

    d.pick_li_answer(a3) # she put sugar
    d.click_continue( ) # . 
    d.click_continue(2) # elle boit son caffee
    d.click_continue(2) # beurk
    d.click_continue(2) # quoi?

    d.pick_li_answer(a4)

    d.click_continue( ) # . 
    d.click_continue(2) # c'est du sel
    d.click_continue(3) # marion tu est tres fatiguee

    d.pick_li_answer(a5)

    d.click_continue( ) # . 

    d.match_tokens()

    d.click_continue( ) # 24XP
    d.click_continue( ) # story complete
    d.click_continue_skip( ) # . 

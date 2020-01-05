import duolingo
import time

a1 = 'My darling.'
a2 = 'examen d\'anglais'
a3 = 'She put sugar in her cup of coffee.'
a4 = 'What?'
a5 = '… put salt in her coffee instead of sugar.'

def init():
    return duolingo.Duolingo('Firefox')

def login(d):
    d.goto_duolingo()
    d.click_alread_have_an_account()
    d.provide_credentials()
    d.click_login()


def run1(d):
    d.switch_to_stories()
    d.start_the_story() 

    d.click_continue() # bonjour
    d.click_continue() # jean est a la maison avec ca femme marion
    d.click_continue() # salut marion
    d.click_continue() # salut mon cheri

    d.pick_li_answer(a1) # My darling
    #d.pick_my_darling()

def run2(d):
    d.click_continue() # .
    d.click_continue() # ou est mon livre d'anglais
    d.click_continue() # pardon + click

    d.pick_li_answer(a2) # examen d'anglais

def run3(d):
    d.click_continue() # . 
    d.click_continue() # ou est mon livre
    d.click_continue() # il est ici,.. sur la table,.. marion + click
    d.click_continue() # (3sec for:)je suis fatiguee jean, je travail beaucoup (+ click)

    d.pick_6th_phrase() # fatigueeee

def run4(d):
    d.click_continue() # . 
    d.click_continue() # tu veux une tasse du cafee?
    d.click_continue() # oui, merci
    d.click_continue() # voila
    d.click_continue() # marion mets du sucre dans ca tasse

    d.pick_li_answer(a3) # she put sugar

def run5(d):
    d.click_continue() # . 
    d.click_continue() # elle boit son caffee
    d.click_continue() # beurk
    d.click_continue() # quoi?

    d.pick_li_answer(a4)

def run6(d):
    d.click_continue() # . 
    d.click_continue(2) # c'est du sel
    d.click_continue(3) # marion tu est tres fatiguee

    d.pick_li_answer(a5)

def run7(d):
    d.click_continue( ) # . 

    d.match_tokens()
    input('all matched? ')
    d.click_continue( ) # 24XP
    d.click_continue( ) # story complete
    d.click_continue_skip( ) # . 


def run(d):
    input("Have you logged in successfully?")
    run1(d)
    run2(d)
    run3(d)
    run4(d)
    run5(d)
    run6(d)
    run7(d)

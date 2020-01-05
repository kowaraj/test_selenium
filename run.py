import duolingo

a1 = 'My darling.'
a2 = 'examen d\'anglais'
a3 = 'She put sugar in her cup of coffee.'
a4 = 'What?'
a5 = '… put salt in her coffee instead of sugar.'

d = duolingo.Duolingo('Firefox')
d.click_alread_have_an_account()
d.provide_credentials()
d.click_login()
d.switch_to_stories()
d.start_the_story()

d.click_continue(2) # bonjour
d.click_continue(3) # jean est a la maison avec ca femme marion
d.click_continue(2) # salut marion
d.click_continue(3) # salut mon cheri
d.click_continue(1) # .

d.pick_li_answer(a1) # My darling
#d.pick_my_darling()

d.click_continue()
d.click_continue()
d.click_continue()

d.pick_li_answer(a2) # fatiguee

d.click_continue()
d.click_continue()
d.click_continue()
d.click_continue()
d.click_continue()

d.pick_li_answer(a3) # she put sugar

d.click_continue()
d.click_continue()
d.click_continue()
d.click_continue()

d.pick_li_answer(a4)

d.click_continue()
d.click_continue()
d.click_continue()

d.pick_li_answer(a5)

d.click_continue()

d.match_tokens()
d.click_continue()
d.click_continue()
d.click_continue()


from random import choice

mood1 = ('gay melancholia', 'sad', 'gay', 'bestests', 'romace', 'mlm')
mood2 = ('lesbian', 'melancholia', 'sad', 'romance', 'lgbtq')
mood3 = ('korean', 'psychological thrillers')

movie = {
    mood1 : ['maurice', 'call me by your name', 'brokeback mountain', 'firebird', 'my own private idaho'],

    mood2 : [ 'colete', 'carol', 'potrait of a lady on fire', 'world to come', 'ride or die' ],

    mood3 : ['oldboy', 'i saw the devil', 'whaling', 'forgotten', 'parasite']

}

mood = input("whats your mood?")

for i in movie:
    if mood == mood1[0:5]:
        print(choice(movie[0]))

    elif mood == mood2[0:4]:
        print(choice(movie[0:1]))

    else:

        print(choice(movie[0:2]))


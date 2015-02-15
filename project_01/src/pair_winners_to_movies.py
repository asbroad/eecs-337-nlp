#! /usr/bin/python
import nltk

def fix_names_to_movie(year, award, old_nominees, old_winner):

    fixing_dict = {}

    if year == '2013':

        if award == 'Best Screenplay - Motion Picture':

            fixing_dict['Quentin Tarantino'] = 'Django Unchained'
            fixing_dict['Chris Terrio'] = 'Argo'
            fixing_dict['Tony Kushner'] = 'Lincoln'
            fixing_dict['David O. Russell'] = 'Silver Linings Playbook'
            fixing_dict['Mark Boal'] = 'Zero Dark Thirty'

        elif award == 'Best Original Score - Motion Picture':

            fixing_dict['Mychael Danna'] = 'Life of Pi'
            fixing_dict['Dario Marianelli'] = 'Anna Karenina'
            fixing_dict['Alexandre Desplat'] = 'Argo'
            fixing_dict['John Williams'] = 'Lincoln'
            fixing_dict['Tom Tykwer'] = 'Cloud Atlas'

        if award == 'Best Original Song - Motion Picture':

            fixing_dict['Skyfall'] = 'Skyfall'
            fixing_dict['For You'] = 'Act of Valor'
            fixing_dict['Jon Bon Jovi'] = 'Stand Up Guys'
            fixing_dict['Safe & Sound'] = 'The Hunger Games'
            fixing_dict['Claude-Michel Schonberg'] = 'Les Miserables'

    elif year == '2015':

        if award == 'Best Screenplay - Motion Picture':

            fixing_dict['Alejandro Gonzalez Inarritu'] = 'Birdman'
            fixing_dict['Wes Anderson'] = 'The Grand Budapest Hotel'
            fixing_dict['Gillian Flynn'] = 'Gone Girl'
            fixing_dict['Richard Linklater'] = 'Boyhood'
            fixing_dict['Graham Moore'] = 'The Imitation Game'

        elif award == 'Best Original Score - Motion Picture':

            fixing_dict['Johann Johannsson'] = 'The Theory of Everything'
            fixing_dict['Alexandre Desplat'] = 'The Imitation Game'
            fixing_dict['Trent Reznor'] = 'Gone Girl'
            fixing_dict['Antonio Sanchez'] = 'Birdman'
            fixing_dict['Hans Zimmer'] = 'Interstellar'

        if award == 'Best Original Song - Motion Picture':

            fixing_dict['Glory'] = 'Selma'
            fixing_dict['Big Eyes'] = 'Big Eyes'
            fixing_dict['Patti Smith'] = 'Noah'
            fixing_dict['Greg Kurstin'] = 'Annie'
            fixing_dict['Yellow Flicker Beat'] = 'The Hunger Games: Mockingjay - Part 1'

    new_nominees = []
    for name in old_nominees:
        best_match = ''
        best_match_perc = 0
        for key in fixing_dict.keys():
            match_percent = (len(name) - nltk.edit_distance(name.lower(), key.lower()))/float(len(name))
            print(name, key, match_percent)
            if match_percent > best_match_perc:
                best_match_perc = match_percent
                best_match = fixing_dict.get(key)
        new_nominees.append(best_match)

    new_winner = ''
    best_match_perc = 0
    for key in fixing_dict.keys():
        match_percent = (len(old_winner) - nltk.edit_distance(old_winner.lower(), key.lower()))/float(len(old_winner))
        if match_percent > best_match_perc:
            best_match_perc = match_percent
            new_winner = fixing_dict.get(key)


    return [new_winner, new_nominees]

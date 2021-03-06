import xml.etree.ElementTree as ET

''' Parse wikipedia for movies '''
def parse_2015_wikipedia_movies(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    body = tree.find('body')
    content_div = body.findall('div')[2]
    body_content_div = content_div.findall('div')[2]
    mw_content_div = body_content_div.findall('div')[3]
    wikitable = mw_content_div.find('table')

    best_movie_row = wikitable.findall('tr')[2]
    best_movie_drama_col = best_movie_row.findall('td')[0]
    best_movies_drama = best_movie_drama_col.findall('.//a')

    best_movies_drama_list = []
    for itm in best_movies_drama:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        movie_name = val_split[0].strip()
        best_movies_drama_list.append(movie_name)

    best_movie_mus_or_com_col = best_movie_row.findall('td')[1]
    best_movies_mus_or_com = best_movie_mus_or_com_col.findall('.//a')

    best_movies_mus_or_com_list = []
    for itm in best_movies_mus_or_com:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        movie_name = val_split[0].strip()
        best_movies_mus_or_com_list.append(movie_name)

    best_actor_row = wikitable.findall('tr')[5]
    best_actor_drama_col = best_actor_row.findall('td')[0]
    best_actor_drama = best_actor_drama_col.findall('.//li')

    best_actor_drama_list = []
    for idx in range(0,len(best_actor_drama)):
        val = best_actor_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_drama_list.append(actor_name)

    best_actress_drama_col = best_actor_row.findall('td')[1]
    best_actress_drama = best_actress_drama_col.findall('.//li')

    best_actress_drama_list = []
    for idx in range(0,len(best_actress_drama)):
        val = best_actress_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_drama_list.append(actress_name)

    best_actor_com_mus_row = wikitable.findall('tr')[8]
    best_actor_com_mus__col = best_actor_com_mus_row.findall('td')[0]
    best_actor_com_mus = best_actor_com_mus__col.findall('.//li')

    best_actor_com_mus_list = []
    for idx in range(0,len(best_actor_com_mus)):
        val = best_actor_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_com_mus_list.append(actor_name)

    best_actress_com_mus__col = best_actor_com_mus_row.findall('td')[1]
    best_actress_com_mus = best_actress_com_mus__col.findall('.//li')

    best_actress_com_mus_list = []
    for idx in range(0,len(best_actress_com_mus)):
        val = best_actress_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_com_mus_list.append(actress_name)

    best_actor_supporting_row = wikitable.findall('tr')[11]
    best_actor_supporting_col = best_actor_supporting_row.findall('td')[0]
    best_actor_supporting = best_actor_supporting_col.findall('.//li')

    best_actor_supporting_list = []
    for idx in range(0,len(best_actor_supporting)):
        val = best_actor_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_supporting_list.append(actor_name)

    best_actress_supporting_col = best_actor_supporting_row.findall('td')[1]
    best_actress_supporting = best_actress_supporting_col.findall('.//li')

    best_actress_supporting_list = []
    for idx in range(0,len(best_actress_supporting)):
        val = best_actress_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_supporting_list.append(actress_name)

    best_director_row = wikitable.findall('tr')[14]
    best_director_col = best_director_row.findall('td')[0]
    best_director = best_director_col.findall('.//li')

    best_director_list = []
    for idx in range(0,len(best_director)):
        val = best_director[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        director_name = val_split[0].strip()
        best_director_list.append(director_name)

    best_screenplay_col = best_director_row.findall('td')[1]
    best_screenplay = best_screenplay_col.findall('.//li')

    best_screenplay_list = []
    for idx in range(0,len(best_screenplay)):
        val = best_screenplay[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        screenplay_title = val_split[0].strip()
        best_screenplay_list.append(screenplay_title)

    best_music_row = wikitable.findall('tr')[16]
    best_music_col = best_music_row.findall('td')[0]
    best_score = best_music_col.findall('.//li')

    best_score_list = []
    for idx in range(0,len(best_score)):
        val = best_score[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        score_title = val_split[0].strip()
        best_score_list.append(score_title)

    best_song_col = best_music_row.findall('td')[1]
    best_song = best_song_col.findall('.//li')

    best_song_list = []
    for idx in range(0,len(best_song)):
        val = best_song[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        song_title = val_split[0].strip()
        best_song_list.append(song_title)

    best_other_row = wikitable.findall('tr')[18]
    best_other_col = best_other_row.findall('td')[0]
    best_animated_film = best_other_col.findall('.//li')

    best_animated_list = []
    for idx in range(0,len(best_animated_film)):
        val = best_animated_film[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        animated_title = val_split[0].strip()
        best_animated_list.append(animated_title)

    best_other_col = best_other_row.findall('td')[1]
    best_foreign = best_other_col.findall('.//li')

    best_foreign_list = []
    for idx in range(0,len(best_foreign)):
        val = best_foreign[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        foreign_title = val_split[0].strip()
        best_foreign_list.append(foreign_title)

    scraped_data = {}
    scraped_data['Best Motion Picture - Drama'] = best_movies_drama_list
    scraped_data['Best Performance by an Actress in a Motion Picture - Drama'] = best_actress_drama_list
    scraped_data['Best Performance by an Actor in a Motion Picture - Drama']  = best_actor_drama_list
    scraped_data['Best Motion Picture - Comedy Or Musical'] = best_movies_mus_or_com_list
    scraped_data['Best Performance by an Actress in a Motion Picture - Comedy Or Musical'] = best_actress_com_mus_list
    scraped_data['Best Performance by an Actor in a Motion Picture - Comedy Or Musical'] = best_actor_com_mus_list
    scraped_data['Best Animated Feature Film'] = best_animated_list
    scraped_data['Best Foreign Language Film'] =best_foreign_list
    scraped_data['Best Performance by an Actress In A Supporting Role in a Motion Picture'] = best_actress_supporting_list
    scraped_data['Best Performance by an Actor In A Supporting Role in a Motion Picture'] = best_actor_supporting_list
    scraped_data['Best Director - Motion Picture'] = best_director_list
    scraped_data['Best Screenplay - Motion Picture'] = best_screenplay_list
    scraped_data['Best Original Score - Motion Picture'] = best_score_list
    scraped_data['Best Original Song - Motion Picture'] = best_song_list

    return scraped_data

''' Parse wikipedia for tv '''
def parse_2015_wikipedia_tv(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    body = tree.find('body')
    content_div = body.findall('div')[2]
    body_content_div = content_div.findall('div')[2]
    mw_content_div = body_content_div.findall('div')[3]
    wikitable = mw_content_div.findall('table')[3]

    best_tv_row = wikitable.findall('tr')[2]
    best_tv_drama_col = best_tv_row.findall('td')[0]
    best_tv_drama = best_tv_drama_col.findall('.//a')

    best_tv_drama_list = []
    for itm in best_tv_drama:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        tv_name = val_split[0].strip()
        best_tv_drama_list.append(tv_name)

    best_tv_mus_or_com_col = best_tv_row.findall('td')[1]
    best_tv_mus_or_com = best_tv_mus_or_com_col.findall('.//a')

    best_tv_mus_or_com_list = []
    for itm in best_tv_mus_or_com:
        val = itm.attrib['title']
        val_minus_wiki = val
        val_fixed = val_minus_wiki.replace('_', ' ')
        val_split = val_fixed.split('(')
        tv_name = val_split[0].strip()
        best_tv_mus_or_com_list.append(tv_name)

    best_actor_row = wikitable.findall('tr')[5]
    best_actor_drama_col = best_actor_row.findall('td')[0]
    best_actor_drama = best_actor_drama_col.findall('.//li')

    best_actor_drama_list = []
    for idx in range(0,len(best_actor_drama)):
        val = best_actor_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_drama_list.append(actor_name)

    best_actress_drama_col = best_actor_row.findall('td')[1]
    best_actress_drama = best_actress_drama_col.findall('.//li')

    best_actress_drama_list = []
    for idx in range(0,len(best_actress_drama)):
        val = best_actress_drama[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_drama_list.append(actress_name)

    best_actor_com_mus_row = wikitable.findall('tr')[8]
    best_actor_com_mus__col = best_actor_com_mus_row.findall('td')[0]
    best_actor_com_mus = best_actor_com_mus__col.findall('.//li')

    best_actor_com_mus_list = []
    for idx in range(0,len(best_actor_com_mus)):
        val = best_actor_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_com_mus_list.append(actor_name)

    best_actress_com_mus__col = best_actor_com_mus_row.findall('td')[1]
    best_actress_com_mus = best_actress_com_mus__col.findall('.//li')

    best_actress_com_mus_list = []
    for idx in range(0,len(best_actress_com_mus)):
        val = best_actress_com_mus[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_com_mus_list.append(actress_name)

    best_actor_miniseries_row = wikitable.findall('tr')[11]
    best_actor_miniseries_col = best_actor_miniseries_row.findall('td')[0]
    best_actor_miniseries = best_actor_miniseries_col.findall('.//li')

    best_actor_miniseries_list = []
    for idx in range(0,len(best_actor_miniseries)):
        val = best_actor_miniseries[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_miniseries_list.append(actor_name)

    best_actress_miniseries_col = best_actor_miniseries_row.findall('td')[1]
    best_actress_miniseries = best_actress_miniseries_col.findall('.//li')

    best_actress_miniseries_list = []
    for idx in range(0,len(best_actress_miniseries)):
        val = best_actress_miniseries[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_miniseries_list.append(actress_name)

    best_actor_supporting_row = wikitable.findall('tr')[14]
    best_actor_supporting_col = best_actor_supporting_row.findall('td')[0]
    best_actor_supporting = best_actor_supporting_col.findall('.//li')

    best_actor_supporting_list = []
    for idx in range(0,len(best_actor_supporting)):
        val = best_actor_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actor_name = val_split[0].strip()
        best_actor_supporting_list.append(actor_name)

    best_actress_supporting_col = best_actor_supporting_row.findall('td')[1]
    best_actress_supporting = best_actress_supporting_col.findall('.//li')

    best_actress_supporting_list = []
    for idx in range(0,len(best_actress_supporting)):
        val = best_actress_supporting[idx].find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        actress_name = val_split[0].strip()
        best_actress_supporting_list.append(actress_name)

    best_miniseries_row = wikitable.findall('tr')[16]
    best_miniseries_col = best_miniseries_row.findall('td')[0]
    best_miniseries = best_miniseries_col.findall('.//li')

    best_miniseries_list = []
    for idx in range(0,len(best_miniseries)):
        val = best_miniseries[idx].find('i').find('a')
        val_title = val.attrib['title']
        val_split = val_title.split('(')
        miniseries_title = val_split[0].strip()
        best_miniseries_list.append(miniseries_title)

    scraped_data = {}
    scraped_data['Best Television Series - Drama'] = best_tv_drama_list
    scraped_data['Best Performance by an Actress In A Television Series - Drama'] = best_actress_drama_list
    scraped_data['Best Performance by an Actor In A Television Series - Drama'] = best_actor_drama_list
    scraped_data['Best Television Series - Comedy Or Musical'] = best_tv_mus_or_com_list
    scraped_data['Best Performance by an Actress In A Television Series - Comedy Or Musical'] = best_actress_com_mus_list
    scraped_data['Best Performance by an Actor In A Television Series - Comedy Or Musical'] = best_actor_com_mus_list
    scraped_data['Best Mini-Series Or Motion Picture Made for Television'] = best_miniseries_list
    scraped_data['Best Performance by an Actress In A Mini-series or Motion Picture Made for Television'] = best_actress_miniseries_list
    scraped_data['Best Performance by an Actor in a Mini-Series or Motion Picture Made for Television'] = best_actor_miniseries_list
    scraped_data['Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television'] = best_actress_supporting_list
    scraped_data['Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television'] = best_actor_supporting_list

    return scraped_data

''' Parse wikipedia for presenters '''
def parse_2015_wikipedia_presenters(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    body = tree.find('body')
    content_div = body.findall('div')[2]
    body_content_div = content_div.findall('div')[2]
    mw_content_div = body_content_div.findall('div')[3]
    presenters_div = mw_content_div.findall('div')[12]
    presenters_ul = presenters_div.findall('ul')[0]
    presenters_il = presenters_ul.findall('li')

    full_names = []
    full_awards = []
    for presenter in presenters_il:
        names = []
        award = []
        last_word_was_introduced = False
        for itm in presenter.itertext():
            if last_word_was_introduced:
                award.append(itm.strip().encode("utf-8"))
                last_word_was_introduced = False
            elif 'introduce' in itm:
                last_word_was_introduced = True
            else:
                if 'with' in itm:
                    award.append(itm.replace('with','').strip().encode("utf-8"))
                else:
                    if 'and' in itm:
                        continue
                    names.append(itm.strip().encode("utf-8"))
        full_names.append(names)
        full_awards.append(award)
    return [full_names, full_awards]


def process_presenters(presenter_list):

    final_presenter_list = []
    final_award_list = []

    for presenters in presenter_list[0]:
        processed_presenter = ""
        for element in presenters:
            processed_presenter = processed_presenter + element + " "
        final_presenter = ""
        split_presenter = processed_presenter.split()
        for item in split_presenter:
            if 64 < ord(item[0]) < 91 or 96 < ord(item[0]) < 123:
                final_presenter = final_presenter + " " + item
        final_presenter_list = final_presenter_list + [final_presenter[1:]]

    for awards in presenter_list[1]:
        processed_award = ""
        for element in awards:
            processed_award = processed_award + element + " "
        final_award = ""
        split_award = processed_award.split()
        for item in split_award:
            if 64 < ord(item[0]) < 91 or 96 < ord(item[0]) < 123:
                final_award = final_award + " " + item
        final_award_list = final_award_list + [final_award[1:]]
    return [final_presenter_list, final_award_list]

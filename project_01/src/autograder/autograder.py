import json
import sys
from nltk.metrics import edit_distance,masi_distance
from collections import Counter
from pprint import pprint

decision_to_methods = {'1': 'hardcoded', '2': 'scraped', '3': 'detected'}
methods_to_decision = {'hardcoded': 1, 'scraped': 2, 'detected': 3}

def calc_translation(result, answer):
    """Accepts two lists of strings and returns a score for how
    closely they match, and a dictionary mapping result list items
    to their closest match in the answer list"""
    intersection = result.intersection(answer)
    len_intersection = len(intersection)
    len_union = len(result.union(answer))
    len_result = len(result)
    len_answer = len(answer)
    new_intersection = len_intersection

    translation = dict(zip(intersection,intersection))
    if len_result == len_answer and len_intersection == len_answer:
        m = 1.0
    elif len_intersection == len_result:
        # all results are correct but some are missing
        m = 0.67
        translation += dict(zip(answer-result,[""]*len(answer-result)))
    elif len_intersection == len_answer:
        # correct results for entire answer list, but some extra
        # results as well
        m = 0.5
    else:
        distance_by_results = {}
        distance_by_answers = dict(zip(answer-result,[Counter()]*len(answer-result)))
        for r in (result - answer):
            distance_by_results[r] = Counter()
            for a in (answer - result):
                distance_by_results[r][a] = edit_distance(a,r)
                distance_by_answers[a][r] = distance_by_results[r][a]
        for r in distance_by_results:
            cnt = -1
            ranking = distance_by_results[r].most_common()
            while r not in translation:
                answer_match = ranking[cnt][0]
                min_result = distance_by_answers[answer_match].most_common()[-1][0]
                max_length = float(max(len(answer_match),len(r)))
                if distance_by_results[r][answer_match] > max_length/2:
                    translation[r] = ""
                elif (min_result == r) or (distance_by_results[r][answer_match] < distance_by_answers[answer_match][min_result]):
                    translation[r] = answer_match
                    new_intersection += distance_by_results[r][answer_match]/max_length
                elif len(ranking) == -1*cnt:
                    translation[r] = ""
                cnt -= 1

        new_result = set([translation[t] for t in translation if translation[t] != ""])
        intersection = new_result.intersection(answer)
        len_intersection = len(intersection)
        len_union = len(new_result.union(answer))
        len_result = len(new_result)

        if len_result == len_answer and len_intersection == len_answer:
            m = 1.0
        elif len_intersection == len_result:
            # all results have a reasonable answer match but some are missing
            m = 0.67
        elif len_intersection == len_answer:
            # all answers have a reasonable result match, but there are
            # some extra results as well
            m = 0.5
        elif len_intersection > 0:
            # when we translate, there is some intersection.
            m = 0.33
        else:
            return 0, translation

        len_intersection = new_intersection

    return (len_intersection / float(len_union)) * m, translation

def check_metadata(item,metadata):
    if (item in metadata) and (metadata[item]['method'] == 'hardcoded'):
        print "The %s were hard coded.\n"%item
    else:
        print item
        print metadata[item]['method']
        print metadata[item]['method_description']
        print "\n1. Treat as hardcoded.\n2. Treat as scraped.\n3. Treat as detected."
        decision = raw_input()
        metadata[item]['method'] = decision_to_methods[decision]

    return metadata            

def lowercase(item):
    for i in item['unstructured']:
        item['unstructured'][i] = [a.lower() for a in item['unstructured'][i]]
    structured = {}
    for award in item['structured']:
        new_award = {}
        for info_type in item['structured'][award]:
            if info_type=='winner':
                new_award[info_type] = item['structured'][award][info_type].lower()
            else:
                new_award[info_type] = [i.lower() for i in item['structured'][award][info_type]]
        structured[award.lower()] = new_award
    item['structured'] = structured

    return item

def main(filename):
    with open(filename, 'r') as f:
        results = json.load(f)
    results['data'] = lowercase(results['data'])

    with open('gg%sanswers.json'%str(results['metadata']['year']),'r') as f:
        answers = lowercase(json.load(f))

    scores = {'unstructured': {},'structured': {}}
    translation = {}
    total = 0

    print "CALCULATING UNSTRUCTURED SCORES"
    print "=============================\n"
    for item in results['data']['unstructured']:
        weight = len(answers['unstructured'][item])
        if item in results['metadata']:
            results['metadata'] = check_metadata(item, results['metadata'])
            weight = weight*(methods_to_decision[results['metadata'][item]['method']]-1.0)/2.0
        if weight != 0:
            score, trans = calc_translation(set(results['data']['unstructured'][item]),set(answers['unstructured'][item]))
            translation.update(trans)
            scores['unstructured'][item] = weight*score
            print "\n%s\t%.2f x %.2f\n"%(item,score,weight)
        total += weight
    scores['unstructured']['overall'] = sum(scores['unstructured'].values())
    scores['unstructured']['total'] = total
    print "-----------------------------"
    print "TOTAL\t%.2f / %.2f\n"%(scores['unstructured']['overall'],total)
    print "\n=============================\n"
    print "CALCULATING STRUCTURED SCORES"
    print "=============================\n"
    nom_scores = {}
    win_scores = {}
    pres_scores = {}
    pres_total = 0
    nom_total = 0
    for a in results['data']['structured']:
        translated = translation[a]
        print translated
        nomlen = len(answers['structured'][translated]['nominees'])
        if nomlen > 0:
            nom_scores[translated] = (1 - masi_distance(set(answers['structured'][translated]['nominees']),set([translation[r] for r in results['data']['structured'][a]['nominees']])))*nomlen
            print "\tNominees:\t%.2f / %d"%(nom_scores[translated],nomlen)
            nom_total += len(answers['structured'][translated]['nominees'])
        preslen = len(answers['structured'][translated]['presenters'])
        pres_scores[translated] = (1 - masi_distance(set(answers['structured'][translated]['presenters']),set([translation[r] for r in results['data']['structured'][a]['presenters']])))*preslen
        pres_total+=preslen
        print "\tPresenters:\t%.2f / %d"%(pres_scores[translated], preslen)
        if answers['structured'][translated]['winner'] == translation[results['data']['structured'][translated]['winner']]:
            win_scores[translated] = 1
        else:
            win_scores[translated] = 0
        print "\tWinner:\t%d"%win_scores[translated]

    print "=============================\n"
    scores['structured']['nominees'] = sum(nom_scores.values())
    scores['structured']['winners'] = sum(win_scores.values())
    scores['structured']['presenters'] = sum(pres_scores.values())
    scores['structured']['overall'] = sum(scores['structured'].values())
    scores['structured']['total'] = nom_total + len(win_scores) + pres_total

    print "Structured nominees score:  \t%.2f / %.2f"%(scores['structured']['nominees'], nom_total)
    print "Structured winners score:   \t%.2f / %.2f"%(scores['structured']['winners'],float(len(win_scores)))
    print "Structured presenters score:\t%.2f / %.2f"%(scores['structured']['presenters'],pres_total)
    print "-----------------------------"
    print "TOTAL                       \t%.2f / %.2f\n"%(scores['structured']['overall'],scores['structured']['total'])
    print "\n=============================\n"
    print "CALCULATING TOTAL SCORES"
    print "=============================\n"

    scores['overall'] = scores['unstructured']['overall'] + scores['structured']['overall']
    scores['total'] = scores['unstructured']['total'] + scores['structured']['total']

    print "TOTAL\t%.2f / %.2f\n"%(scores['overall'],scores['total'])

    with open('gg%sscores.json'%str(results['metadata']['year']),'w') as f:
        json.dump(scores,f)

if __name__ == '__main__':
    main(sys.argv[1])
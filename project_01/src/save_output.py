import json

def save_output(year, hosts_in, all_winners_in, all_awards_in, all_presenters_in, all_nominees_in, all_structured_awards, output_filename):

    formatted_results = {}

    metadata = {}
    hosts = {
        'method':  'detected',
        'method_description': 'searched for names that co-occured with the word host'
    }

    nominees = {
        'method':  'scraped',
        'method_description': 'scraped from wikipedia'
    }

    awards = {
        'method':  'scraped',
        'method_description': 'scraped from wikipedia'
    }

    presenters = {
        'method':  'scraped',
        'method_description': 'scraped from wikipedia'
    }

    metadata['year'] = year
    metadata['hosts'] = hosts
    metadata['nominees'] = nominees
    metadata['awards'] = awards
    metadata['presenters'] = presenters

    data = {}

    unstructured = {}
    unstructured['hosts'] = hosts_in
    unstructured['winners'] = all_winners_in
    unstructured['awards'] = all_awards_in
    unstructured['presenters'] = all_presenters_in
    unstructured['nominees'] = all_nominees_in

    structured = {}

    for structured_award in all_structured_awards:
        for key, value in structured_award.iteritems():
            structured[key] = value

    data['unstructured'] = unstructured
    data['structured'] = structured

    formatted_results['metadata'] = metadata
    formatted_results['data'] = data

    with open(output_filename, 'w') as outfile:
        json.dump(formatted_results, outfile)

    print('Finished writing to file : ', output_filename)

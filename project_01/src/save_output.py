import json

def save_output(year, hosts_in, all_winners_in, all_awards_in, all_presenters_in, all_nominees_in, all_structured_awards, output_filename):

    formatted_results = {}

    hosts = {
        'method':  'detected',
        'method_description': 'We searched over the entire tweet dataset, and returned an ordered list based on a count of the co-occurance of the word *host* and bi-gram proper nouns.  We then return the top two results as there are two hosts.  The number of hosts is a parameter that can be set for each year.'
    }

    nominees = {
        'method':  'scraped',
        'method_description': 'We scrapped the nominees for each award from Wikipedia.  Wikipedia follows the same format for both the table they produce in both 2013 and 2015.'
    }

    awards = {
        'method':  'scraped',
        'method_description': 'Again, we scrapped the award titles from Wikipedia.'
    }

    presenters = {
        'method':  'scraped',
        'method_description': 'And again, we scrapped the presenters from a list currated on Wikipedia'
    }

    names = {}

    names['hosts'] = hosts
    names['nominees'] = nominees
    names['awards'] = awards
    names['presenters'] = presenters

    mappings = {}

    nominees_map = {
        'method':  'detected',
        'method_description': 'We used the Levenshtein distance to calculate the difference between our detected results and the scrapped nominees'
    }

    presenters_map = {
        'method':  'detected',
        'method_description': 'Again, we used the Levenshtein distance to calculate the difference between our detectsion and the scrapped presenter list'
    }

    mappings['nominees'] = nominees_map
    mappings['presenters'] = presenters_map

    metadata = {}
    metadata['year'] = year
    metadata['names'] = names
    metadata['mappings'] = mappings

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

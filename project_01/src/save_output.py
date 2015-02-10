import json

def save_output(output_filename):

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

    metadata['year'] = 'test'# year
    metadata['hosts'] = hosts
    metadata['nominees'] = nominees
    metadata['awards'] = awards
    metadata['presenters'] = presenters

    data = {}

    unstructured = {}
    unstructured['hosts'] = 'test'# hosts
    unstructured['winners'] = 'test'# winners
    unstructured['awards'] = 'test'# awards
    unstructured['presenters'] = 'test'# presenters
    unstructured['nominees'] = 'test'# nominees

    structured = {}
    award1 = {}
    award1['nominees'] = 'test'# nominees
    award1['winner'] = 'test'# winner
    award1['presenters'] = 'test'# presenters

    structured['award1'] = award1

    data['unstructured'] = unstructured
    data['structured'] = structured

    formatted_results['metadata'] = metadata
    formatted_results['data'] = data

    with open(output_filename, 'w') as outfile:
        json.dump(formatted_results, outfile)

    print('Finished writing to file : ', output_filename)

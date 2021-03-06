catagories = [
    'host',
    'best movie drama',
    'best movie musical or comedy',
    'best actor drama',
    'best actress drama',
    'best actor musical or comedy',
    'best actress musical or comedy',
    'best supporting actor',
    'best supporting actress',
    'best director',
    'best screenplay',
    'best original score',
    'best original song',
    'best animated movie',
    'best foreign movie',
    'best tv series drama',
    'best tv musical or comedy',
    'best actor tv drama',
    'best actress tv drama',
    'best actor tv musical or comedy',
    'best actress tv musical or comedy',
    'best actor tv movie',
    'best actress tv movie',
    'best supporting actor tv movie',
    'best supporting actress tv movie',
    'best tv movie'
]

''' Hand coded 2015 data, the first value in each array is the winner '''
def get_academy_info():
    truth_data = {}
    performer_movie = {}

    truth_data['best movie drama'] = ['boyhood', 'foxcatcher', 'the imitation game', 'selma', 'the theory of everything']
    truth_data['best actress drama'] = ['julianne moore', 'rosamund pike', 'reese witherspoon', 'felicity jones', 'jenifer aniston']
    truth_data['best actor drama']  = ['eddie redmayne', 'steve carell', 'benedict cumberbatch', 'david oyelowo', 'jake gyllenhaal']
    truth_data['best movie musical or comedy'] = ['the grand budapest hotel', 'into the woods', 'birdman', 'st. vincent', 'pride']
    truth_data['best actress musical or comedy'] = ['amy adams', 'julianne moore', 'emily blunt', 'helen mirren', 'quvenzhane wallis']
    truth_data['best actor musical or comedy'] = ['michael keaton', 'bill murray', 'ralph fiennes', 'christoph waltz', 'joaquin phoenix']
    truth_data['best animated movie'] = ['how to train your dragon 2', 'the lego movie', 'big hero 6', 'the book of life', 'the boxtrolls']
    truth_data['best foreign movie'] = ['leviathan', 'ida', 'force majeure', 'gett: the trial of viviane amsalem', 'tangerines']
    truth_data['best supporting actress'] = ['patricia arquette', 'jessica chastain', 'keira knightley', 'meryl streep', 'emma stone']
    truth_data['best supporting actor'] = ['j.k. simmons', 'ethan hawke', 'robert duvall', 'edward norton', 'mark ruffalo']
    truth_data['best directory'] = ['richard linklater', 'ava duvernay', 'wes anderson', 'alejandro gonzalez inarritu', 'david fincher']
    truth_data['best screenplay'] = ['alejandro gonzalez inarritu, nicolas giacobone, alexander dinelaris, armando bo', 'wes anderson', 'gillian flynn', 'richard linklater', 'graham moore']
    truth_data['best original score'] = ['johann johannsson', 'alexandre desplat', 'trent reznor, atticus ross', 'antonio sanchez', 'hans zimmer']
    truth_data['best original song'] = ['selma', 'big eyes', 'noah', 'annie', 'the hunger games: mockingjay, part 1']
    truth_data['best tv series drama'] = ['the affair', 'downton abbey', 'game of thrones', 'house of cards', 'the good wife']
    truth_data['best actress tv drama'] = ['ruth wilson', 'viola davis', 'claire danes', 'julianna margulies', 'robin wright']
    truth_data['best actor tv drama'] = ['kevin spacey', 'clive owen', 'james spader', 'dominic west', 'liev schreiber']
    truth_data['best tv musical or comedy'] = ['transparent', 'orange is the new black', 'girls', 'jane the virgin', 'silicon valley']
    truth_data['best actress tv musical or comedy'] = ['gina roderiguez', 'julia louis-dreyfus', 'edie falco', 'lena dunham', 'taylor schilling']
    truth_data['best actor tv musical or comedy'] = ['jeffrey tambor', 'don cheadle', 'william h. macy', 'ricky gervais', 'louis c.k.']
    truth_data['best tv movie'] = ['fargo', 'olive kitteridge', 'the missing', 'true detective', 'the normal heart']
    truth_data['best actress tv movie'] = ['maggie gyllenhaal', 'jessica lange', 'france mcdormand', 'allison tolman', 'frances o\'connor']
    truth_data['best actor tv movie'] = ['billy bob thornton', 'martin freeman', 'matthew mcconaughey', 'woody harrelson', 'mark ruffalo']
    truth_data['best supporting actress tv movie'] = ['joanne froggatt', 'kathy bates', 'uzo aduba', 'michelle monaghan', 'allison janney']
    truth_data['best supporting actor tv movie'] = ['matt bomer', 'bill murray', 'jon voight', 'alan cumming', 'colin hanks']

    performer_movie['julianne moore'] = 'still alice'
    performer_movie['rosamund pike'] = 'gone girl'
    performer_movie['reese witherspoon'] = 'wild'
    performer_movie['felicity jones'] = 'the theory of everything'
    performer_movie['jennifer aniston'] = 'cake'
    performer_movie['eddie redmayne'] = 'the theory of everything'
    performer_movie['steve carell'] = 'foxcatcher'
    performer_movie['benedict cumberbatch'] = 'the imitation game'
    performer_movie['david oyelowo'] = 'selma'
    performer_movie['jake gyllenhaal'] = 'nightcrawler'
    performer_movie['julianne moore'] = 'maps to the stars'
    performer_movie['amy adams'] = 'big eyes'
    performer_movie['emily blunt'] = 'into the woods'
    performer_movie['helen mirren'] = 'the hundred foot journey'
    performer_movie['quvenzhane wallis'] = 'annie'
    performer_movie['michael keaton'] = 'birdman'
    performer_movie['bill murray'] = 'st. vincent'
    performer_movie['ralph fiennes'] = 'the grand budapest hotel'
    performer_movie['christoph waltz'] = 'big eyes'
    performer_movie['joaquin phoenix'] = 'inherent vice'
    performer_movie['jessica chastain'] = 'a most violent year'
    performer_movie['keira knightley'] = 'the imitation game'
    performer_movie['patricia arquette'] = 'boyhood'
    performer_movie['meryl streep'] = 'into the woods'
    performer_movie['emma stone'] = 'birdman'
    performer_movie['ethan hawke'] = 'boyhood'
    performer_movie['robert duvall'] = 'the judge'
    performer_movie['edward norton'] = 'birdman'
    performer_movie['j.k. simmons'] = 'whiplash'
    performer_movie['mark ruffalo'] = 'foxcatcher'
    performer_movie['ava duvernay'] = 'selma'
    performer_movie['wes anderson'] = 'the grand budapest hotel'
    performer_movie['alejandro gonzalez inarritu'] = 'birdman'
    performer_movie['david fincher'] = 'gone girl'
    performer_movie['richard linklater'] = 'boyhood'
    performer_movie['wes anderson'] = 'the grand budapest hotel'
    performer_movie['gillian flynn'] = 'gone girl'
    performer_movie['alejandro gonzalez inarritu, nicolas giacobone, alexander dinelaris, armando bo'] = 'birdman'
    performer_movie['richard linklater'] = 'boyhood'
    performer_movie['graham moore'] = 'the imitation game'
    performer_movie['alexandre desplat'] = 'the imitation game'
    performer_movie['johann johannsson'] = 'the theory of everything'
    performer_movie['trent reznor, atticus ross'] = 'gone girl'
    performer_movie['antonio sanchez'] = 'birdman'
    performer_movie['hans zimmer'] = 'interstellar'
    performer_movie['viola davis'] = 'how to get away with murder'
    performer_movie['claire danes'] = 'homeland'
    performer_movie['julianna margulies'] = 'the good wife'
    performer_movie['robin wright'] = 'house of cards'
    performer_movie['ruth wilson'] = 'the affiar'
    performer_movie['kevin spacey'] = 'house of cards'
    performer_movie['clive owen'] = 'the knick'
    performer_movie['james spader'] = 'the blacklist'
    performer_movie['dominic west'] = 'the affair'
    performer_movie['liev schreiber'] = 'ray donovan'
    performer_movie['julia louis dreyfus'] = 'veep'
    performer_movie['edie falco'] = 'nurse jackie'
    performer_movie['gina roderiguez'] = 'jane the virgin'
    performer_movie['lena dunham'] = 'girls'
    performer_movie['taylor schilling'] = 'orange is the new black'
    performer_movie['don cheadle'] = 'house of lies'
    performer_movie['william h. macy'] = 'shameless'
    performer_movie['ricky gervais'] = 'derek'
    performer_movie['jeffrey tambor'] = 'transparent'
    performer_movie['louis c.k.'] = 'louie'
    performer_movie['jessica lange'] = 'american horror story: freak show'
    performer_movie['maggie gyllenhaal'] = 'the honorable woman'
    performer_movie['frances mcdorman'] = 'olive kitteridge'
    performer_movie['allison tolman'] = 'fargo'
    performer_movie['frances o\'connor'] = 'the missing'
    performer_movie['martin freeman'] = 'fargo'
    performer_movie['matthew mcconaughey'] = 'true detective'
    performer_movie['billy bob thornton'] = 'fargo'
    performer_movie['mark ruffalo'] = 'the normal heart'
    performer_movie['kathy bates'] = 'american horror story: freak show'
    performer_movie['uzo aduba'] = 'orange is the new black'
    performer_movie['joanne froggatt'] = 'downton abbey'
    performer_movie['michelle monaghan'] = 'true detective'
    performer_movie['allison janney'] = 'mom'
    performer_movie['bill murray'] = 'olive kitteridge'
    performer_movie['jon voight'] = 'ray donovan'
    performer_movie['matt bomar'] = 'the normal heart'
    performer_movie['alan cumming'] = 'the good wife'
    performer_movie['colin hanks'] = 'fargo'

    return [truth_data, performer_movie]

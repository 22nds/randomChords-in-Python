# /home/username/example.com/passenger_wsgi.py
# Display random CAGED guitar chords on refresh

import random

#1 Live version on python.princessdesign.net
def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    
    chords = ["C", "A", "G", "E", "D"] 
    random.shuffle(chords)
    return chords
'''
#2 print all chords 50 times in a list

chords = ["C", "A", "G", "E", "D"]
for chord in range(1,50):
    random.shuffle(chords)
    print(chords)


#3 print all chords in a friendly way

chords = ["C", "A", "G", "E", "D"]
for chord in range(1,10):
    random.shuffle(chords)

    for chord in chords:
        print(chord, end='' + ' ')
    print('\r')  # all chords in their own lines - for more space use \n
'''
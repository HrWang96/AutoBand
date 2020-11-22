"""
identifier.py contains the functions used to identify:
    
    1. note (A, A#, B, C, C#, etc)
    
    2. chord (major triad, minor triad, major 7th, etc)
"""


# DEFENITIONS
# assigning midi values to notes
cnotes = [36,48,60,72,84]
csnotes = [x + 1 for x in cnotes]
dnotes = [x + 2 for x in cnotes]
dsnotes = [x + 3 for x in cnotes]
enotes = [x + 4 for x in cnotes]
fnotes = [x + 5 for x in cnotes]
fsnotes = [x + 6 for x in cnotes]
gnotes = [x + 7 for x in cnotes]
gsnotes = [x + 8 for x in cnotes]
anotes = [x + 9 for x in cnotes]
asnotes = [x + 10 for x in cnotes]
bnotes = [x + 11 for x in cnotes]

# chord definitions
majTri = [0,4,7]
majSix = [0,4,7,9]
domSev = [0,4,7,10]
majSev = [0,4,7,11]
augTri = [0,4,8]
augSev = [0,4,8,10]
minTri = [0,3,7]
minSix = [0,3,7,9]
minSev = [0,3,7,10]
minMajSev = [0,3,7,11]
dimTri = [0,3,6]
dimSev = [0,3,6,9]
halfDimSev = [0,3,6,10]
# END DEFENITIONS


# checks the chord for the basenote
def noteCheck(notes):
    notes.sort()
    base = notes[0]
    
    if base in cnotes:
        return('C')
    elif base in csnotes:
        return('C#')
    elif base in dnotes:
        return('D')
    elif base in dsnotes:
        return('D#')
    elif base in enotes:
        return('E')
    elif base in fnotes:
        return('F')
    elif base in fsnotes:
        return('F#')
    elif base in gnotes:
        return('G')
    elif base in gsnotes:
        return('G#')
    elif base in anotes:
        return('A')
    elif base in asnotes:
        return('A#')
    elif base in bnotes:
        return('B')


# checks the spacing between the notes to identify the chord
def chordCheck(notes):
    base = notes[0]
    # checks the chord type
    notes = [x - base for x in notes]
    if notes == majTri:
        return(' Major Triad')
    elif notes == majSix:
        return(' Major Sixth Chord')
    elif notes == domSev:
        return(' Dominant Seventh Chord')
    elif notes == majSev:
        return(' Major Seventh Chord')
    elif notes == augTri:
        return(' Augmented Triad')
    elif notes == augSev:
        return(' Augmented Seventh Chord')
    elif notes == minTri:
        return(' Minor Triad')
    elif notes == minSix:
        return(' Minor Sixth Chord')
    elif notes == minSev:
        return(' Minor Seventh Chord')
    elif notes == minMajSev:
        return(' Minor-Major Seventh Chord')
    elif notes == dimTri:
        return(' Diminished Triad')
    elif notes == dimSev:
        return(' Diminished Seventh Chord')
    elif notes == halfDimSev:
        return(' Half-diminished Seveneth Chord')
    else:
        return(' note')
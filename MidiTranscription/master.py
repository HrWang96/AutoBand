"""
master.py recieves the midi input and 
routes it to the proper functions
"""


import mido
import midiparser
import identifier

notesPlay = []
# inport = mido.open_input()
mid = mido.MidiFile("../Audio-to-midi/output/054.mid")

# logs the midi input as the msg variable
# msg = inport.receive()
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)



# handles the input and sends to midiparser.py to parse
# for msg in inport:
for i, track in enumerate(mid.tracks):
    if i == 2:
        for msg in track:
            try:
                notesPlay = midiparser.refresh(notesPlay, midiparser.parse(msg))
                if notesPlay != []:
                    print(identifier.noteCheck(notesPlay) + identifier.chordCheck(notesPlay))
            except:
                continue


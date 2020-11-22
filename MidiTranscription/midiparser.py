# parses the input into note number (- means note_off)
def parse(midi):    
    if midi.type == 'note_off':
        return -1 * midi.note
    
    else:    
        return midi.note

# alters the list of active notes based on midi input
def refresh(notesList, note):
    if note < 0 and (abs(note) in notesList):
        notesList.remove(abs(note))
        return notesList
    elif note < 0 and (abs(note) not in notesList):
        return notesList
    else:
        notesList.append(note)
        return notesList
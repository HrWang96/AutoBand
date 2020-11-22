import miditoolkit
import utils

midi_obj = miditoolkit.midi.parser.MidiFile('../Audio-to-midi/output/054.mid')

# print(*midi_obj.instruments[0].notes, sep='\n')

# print(*midi_obj.tempo_changes[:10], sep='\n')

note_items, tempo_items = utils.read_items('../Audio-to-midi/output/054.mid')

# print(*note_items, sep='\n')

# print(*tempo_items[:10], sep='\n')

note_items = utils.quantize_items(note_items)

print(*note_items, sep='\n')

chord_items = utils.extract_chords(note_items)

print(*chord_items, sep='\n')


items = chord_items + tempo_items + note_items
max_time = note_items[-1].end
groups = utils.group_items(items, max_time)

for g in groups:
    print(*g, sep='\n')
    print()


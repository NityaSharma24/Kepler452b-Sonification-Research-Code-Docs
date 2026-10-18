import pandas as pd
import math
from mido import MetaMessage, MidiFile, MidiTrack, bpm2tempo, Message

values = df["FLUX"].apply(math.floor).tolist()

window = 5

binned = [
    sum(values[i:i+window]) / len(values[i:i+window])
    for i in range(0, len(values), window)
]

mode_value = pd.Series(binned).mode().iloc[0]
center = mode_value

deviations = [(v - center) for v in binned]

center_midi = 65
raw_notes = [center_midi + int(d) for d in deviations]

LOW = 48
HIGH = 84
midi_notes = [max(LOW, min(HIGH, n)) for n in raw_notes]

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(MetaMessage("set_tempo", tempo=bpm2tempo(160)))
track.append(Message("program_change", program=0, time=0))

note_duration = 120

for note in midi_notes:
    track.append(Message("note_on", note=note, velocity=70, time=0))
    track.append(Message("note_off", note=note, velocity=70, time=note_duration))

mid.save("kepler452b_accessible_sonificationn.mid")

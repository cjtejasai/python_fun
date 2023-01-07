import mido
from midiutil.MidiFile import MIDIFile

# Create a new MIDI file
midi = MIDIFile(3)  # 3 tracks: main theme, drums, bass

# Add the main theme track
track = 0
time = 0
midi.addTrackName(track, time, "Game of Thrones Track")
midi.addTempo(track, time, 120)

# Add the main theme from the "Game of Thrones" TV series
channel = 0
pitch = 60  # Middle C
duration = 1.0
volume = 100

# Repeat the theme for the full length of the track
for i in range(16):  # The theme has a length of 8 measures, so repeat it twice to fill the track
    # First measure
    time = i * 8
    midi.addNote(track, channel, pitch, time, duration, volume)
    time += duration
    midi.addNote(track, channel, pitch + 4, time, duration, volume)
    time += duration
    midi.addNote(track, channel, pitch + 7, time, duration, volume)
    time += duration
    midi.addNote(track, channel, pitch + 12, time, duration, volume)

    # Second measure
    time += duration
    midi.addNote(track, channel, pitch + 12, time, duration, volume)
    time += duration
    midi.addNote(track, channel, pitch + 7, time, duration, volume)
    time += duration
    midi.addNote(track, channel, pitch + 4, time, duration, volume)
    time += duration
    midi.addNote(track, channel, pitch, time, duration, volume)

# Add the drums track
track = 1
channel = 9  # Percussion channel

# Add a simple 4/4 beat with a kick drum on beats 1 and 3, and a snare drum on beats 2 and 4
for i in range(16):
    time = i * 4
    midi.addNote(track, channel, 36, time, 1.0, 100)  # Kick drum
    time += 2
    midi.addNote(track, channel, 38, time, 1.0, 100)  # Snare drum

# Add the bass track
track = 2
channel = 0

# Add a simple 4/4 bass line with root notes on beats 1 and 3, and fifths on beats 2 and 4
for i in range(16):
    time = i * 4
    midi.addNote(track, channel, pitch, time, 1.0, 100)  # Root note
    time += 2
    midi.addNote(track, channel, pitch + 7, time, 1.0, 100)  # Fifth

# Save the MIDI file
with open("game_of_thrones.mid", "wb") as f:
    midi.writeFile(f)

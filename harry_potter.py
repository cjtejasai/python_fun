import random
import mido
from midiutil.MidiFile import MIDIFile

# Generate the Fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci_series = [fibonacci(n) for n in range(10)]
print(fibonacci_series)

# Define the step function
def step(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

# Create a new MIDI file
midi = MIDIFile(1)

# Add a track
track = 0
time = 0
midi.addTrackName(track, time, "Harry Potter + Fast Beats + Random + Fibonacci + Step Track")
midi.addTempo(track, time, 180)  # Increase the tempo to 180 BPM

# Add the "Hedwig's Theme" from the Harry Potter series
with open("hedwig.mid", "rb") as f:
    hedwig = mido.MidiFile.from_file(f)
    hedwig_track = hedwig.tracks[0]
    hedwig_time = 0
    for event in hedwig_track:
        hedwig_time += event.time
        if event.type == "note_on":
            midi.addNote(track, event.channel, event.note, hedwig_time, event.time, event.velocity)

# Add notes based on the random function, Fibonacci series, and step function
channel = 0
for i, pitch in enumerate(fibonacci_series):
    time = hedwig_time + i
    duration = 0.5  # Reduce the note duration to 0.5 beats
    volume = 100
    pitch += step(i-5) * 60 + random.randint(-30, 30)
    pitch = min(max(0, pitch), 127)
    volume = min(max(0, volume), 127)
    midi.addNote(track, channel, pitch, time, duration, volume)

# Extend the track to 3 minutes
for i in range(60 * 3 * 2 - len(fibonacci_series)):  # Multiply by 2 to match the higher tempo
    time = hedwig_time + len(fibonacci_series) + i
    duration = 0.5  # Reduce the note duration to 0.5 beats
    pitch = random.randint(0, 127)
    volume = random.randint(0, 127)
    pitch = min(max(0, pitch), 127)
    volume = min(max(0, volume), 127)
    midi.addNote(track, channel, pitch, time, duration, volume)

# Save the MIDI file
with open("output_harry.mid", "wb") as f:
    midi.writeFile(f)

from midiutil.MidiFile import MIDIFile
import random

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
midi.addTrackName(track, time, "Random + Fibonacci + Step Track")
midi.addTempo(track, time, 120)

# Add notes based on the random function, Fibonacci series, and step function
channel = 0
# Add notes based on the random function, Fibonacci series, and step function
channel = 0
for i, pitch in enumerate(fibonacci_series):
    time = i
    duration = 1
    volume = 100
    pitch += step(i-5) * 60 + random.randint(-30, 30)
    volume = min(max(0, volume), 127)
    pitch = min(max(0, pitch), 127)
    midi.addNote(track, channel, pitch, time, duration, volume)

# Extend the track to 3 minutes
for i in range(60 * 3 - len(fibonacci_series)):
    time = len(fibonacci_series) + i
    duration = 1
    pitch = random.randint(0, 127)
    volume = random.randint(0, 127)
    pitch = min(max(0, pitch), 127)
    volume = min(max(0, volume), 127)
    midi.addNote(track, channel, pitch, time, duration, volume)

# Save the MIDI file
with open("output.mid", "wb") as f:
    midi.writeFile(f)

#import python-midi
import midi
#print(midi._file_)

pattern=midi.Pattern()
track=midi.Track()
pattern.append(track)
on=midi.NoteOnEvent(tick=0, velocity=20, pitch=midi.C_5)
track.append(on)
off=midi.NoteOffEvent(tick=100, pitch=midi.C_5)
track.append(off)
eot=midi.EndOfTrackEvent(tick=1)
track.append(eot)
print pattern
midi.write_midifile("keyboard-midi/midi_files/C5.mid", pattern)

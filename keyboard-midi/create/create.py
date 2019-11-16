import midi
import pygame
import sys
#from pygame import *
pygame.init()
pygame.font.init()


width=1000
height=300
screen=pygame.display.set_mode((width,height))
font = pygame.font.Font(pygame.font.get_default_font(), 36)
#pygame.quit()

pattern=midi.Pattern()
track=midi.Track()
pattern.append(track)

whitekeys=['C','D','E','F','G','A','B','C']
whitenotes=[midi.C_4,midi.D_4,midi.E_4,midi.F_4,midi.G_4,midi.A_4,midi.B_4,midi.C_5]
rollingtick=0
whiteticks=[0,0,0,0,0,0,0,0]

while True:
    keys=pygame.key.get_pressed()
    screen.fill(pygame.Color("black"))
    rollingtick +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    if keys[pygame.K_s]:
        text_surface = font.render(whitekeys[0],True,(255,255,255))
        screen.blit(text_surface, dest=(0,0))
        pygame.display.update()
        """whiteticks[0] +=1
        on=midi.NoteOnEvent(tick=rollingtick, velocity=20, pitch=whitenotes[0])
        track.append(on)"""
        pygame.mixer.music.load("keyboard-midi/midi_files/C4.mid")
        pygame.mixer.music.play()
    elif keys[pygame.K_d]:
        text_surface = font.render(whitekeys[1],True,(255,255,255))
        screen.blit(text_surface,dest=(0,0))
        pygame.display.update()
        """whiteticks[1] +=1
        on=midi.NoteOnEvent(tick=rollingtick, velocity=20, pitch=whitenotes[1])
        track.append(on)"""
        pygame.mixer.music.load("keyboard-midi/midi_files/D4.mid")
        pygame.mixer.music.play()
    elif keys[pygame.K_f]:
        text_surface = font.render(whitekeys[2],True,(255,255,255))
        screen.blit(text_surface,dest=(0,0))
        pygame.display.update()
        """whiteticks[2] +=1
        on=midi.NoteOnEvent(tick=rollingtick, velocity=20, pitch=whitenotes[2])
        track.append(on)"""
        pygame.mixer.music.load("keyboard-midi/midi_files/E4.mid")
        pygame.mixer.music.play()
    elif keys[pygame.K_g]:
        text_surface = font.render(whitekeys[3],True,(255,255,255))
        screen.blit(text_surface,dest=(0,0))
        pygame.display.update()
        #whiteticks[3] +=1
        pygame.mixer.music.load("keyboard-midi/midi_files/F4.mid")
        pygame.mixer.music.play()
    elif keys[pygame.K_h]:
        text_surface = font.render(whitekeys[4],True,(255,255,255))
        screen.blit(text_surface,dest=(0,0))
        pygame.display.update()
        #whiteticks[4] +=1
        pygame.mixer.music.load("keyboard-midi/midi_files/G4.mid")
        pygame.mixer.music.play()
    elif keys[pygame.K_j]:
        text_surface = font.render(whitekeys[5],True,(255,255,255))
        screen.blit(text_surface,dest=(0,0))
        pygame.display.update()
        #whiteticks[5] +=1
        pygame.mixer.music.load("keyboard-midi/midi_files/A4.mid")
        pygame.mixer.music.play()
    elif keys[pygame.K_k]:
        text_surface = font.render(whitekeys[6],True,(255,255,255))
        screen.blit(text_surface,dest=(0,0))
        pygame.display.update()
        #whiteticks[6] +=1
        pygame.mixer.music.load("keyboard-midi/midi_files/B4.mid")
        pygame.mixer.music.play()
    elif keys[pygame.K_l]:
        text_surface = font.render(whitekeys[7],True,(255,255,255))
        screen.blit(text_surface,dest=(0,0))
        pygame.display.update()
        #whiteticks[7] +=1
        pygame.mixer.music.load("keyboard-midi/midi_files/C5.mid")
        pygame.mixer.music.play()
    elif keys[pygame.K_PERIOD]:
        """eot=midi.EndOfTrackEvent(tick=1)
        track.append(eot)
        #print pattern
        midi.write_midifile("keyboard-midi/midi_files/pianoexample.mid", pattern)"""
    else:
        text_surface = font.render('Hello world',True,(255,255,255))
        screen.blit(text_surface, dest=(0,0))
        pygame.display.update()
        """off=midi.NoteOffEvent(tick=rollingtick+whiteticks[0], velocity=20, pitch=whitenotes[0])
        track.append(off)
        off=midi.NoteOffEvent(tick=rollingtick+whiteticks[1], velocity=20, pitch=whitenotes[1])
        track.append(off)
        off=midi.NoteOffEvent(tick=rollingtick+whiteticks[2], velocity=20, pitch=whitenotes[2])
        track.append(off)"""

import sys

sys.path.append('C\Annie\Python2.7\Lib\site-packages')

import numpy as np #image manipulation
import cv2 #image manipulation
import mingus.extra.lilypond as Lilypond #music manipulation
import mingus.core.notes as notes #music manipulation
import musicAndColor as musc #image to music data
import Music as muscno #bass chords
import random
from melopy import Melopy #sounds
from averageColor import averageColorGrid #image data
from averageColor import ImageDimensions #image data
from cvHistExample import showHistogram #image data
from histToNote import showMeTheNote #melody

#Global variables
image_filename = raw_input("Enter the image filename: ")
avg_image_filename = "Average-Color-" + image_filename[:len(image_filename)-4] + ".png"
filename_lily = "testSheet-" + image_filename[:len(image_filename)-4] + ".ly" #sheet music for bass chords
filename_melopy = image_filename[:len(image_filename)-4] + ".mlp" #mlp file for music
print("Image filename: " + image_filename)
print("Average color image filename: " + avg_image_filename)
print("Music sheet filename: " + filename_lily)
print("MLP sheet filename: " + filename_melopy)

n = 5

img = cv2.imread(image_filename) #turn image into numbers
img_dim = ImageDimensions(img, n) #get dimensions of image
img_avg = cv2.imread(avg_image_filename) #make average color image
most_avg = musc.more_average(img_avg) #get most average color of aveage color image
octave = musc.pick_octave(img_avg) #pick an octave
key = musc.pick_key(most_avg) #pick a key using most average color

#Set major_boolean and major variables
if musc.pick_major(img_avg, n) == "major":
    major_boolean = True
    major = "major"
else:
    major_boolean = False
    major = "minor"

print("Most average color: ", most_avg)
#print("Octave: ", octave)
print("Major: ", major_boolean)
print("Key: ", key)

#Key: fixes the sharp/flat problem for Lilypond's music syntax
if len(key) > 0:
    if key[1] == 'b':
        temp_key = key[0]+'es'
    else:
        temp_key = key[0]+'is'

#Variables for writing Lilypond music sheet and mlp file
temp_key = temp_key.lower()
#Generatures the sheet music
track = muscno.create_random_track(key, major_boolean)
lilypitchu = "" #holds music sheet information
melody_melopy = "" #holds melody notes
#bandaid solution for bass:
#I don't know how to play chords in melopy so I'm just going to add 3 tracks
bass1_melopy = ""
bass2_melopy = ""
bass3_melopy = ""
bass_length = 2
version = "\\version \"2.16.0\"  % necessary for upgrading to future LilyPond versions." #REQUIRED to run w/ Lilypond
#Note to annie: before i thought lilypond key didn't accept xb or x#. but for xb you do xes. for flat. and xis is for sharp.

with open(filename_lily,'w') as w:

    w.write(version + "\n")
    w.write("\\header{")
    w.write("  title = \"" + filename_lily + "\"")
    w.write("  subtitle = \"pictoMelody\"")
    w.write("  }") #header closing brackets
    w.write("{\n") #opening brakets

    w.write("  <<\n    \\new Staff\n      \\relative c'\n      {\n") #staff opening brackets
    w.write("        \\key " + temp_key + "\n") #key
    w.write("        \\" + major + "\n") #major/minor
    w.write("        \\clef \"treble\"\n") #treble/bass
    w.write("        \\time 4/4\n          ") #time signature

    #melody
    i = 1
    melody_count = 0
    while (melody_count < 32):
        melody_note = showMeTheNote(img)
        melody_note = melody_note[0]
        #for mlp
        irand = random.randint(0,2)
        if irand == 1 and melody_note > 'A': #go down
            melody_melopy += melody_note + " " + chr(ord(melody_note[0])-1) + " "
            w.write(melody_note[:1].lower() + str(4) + " ")
            w.write(chr(ord(melody_note[:1].lower())-1) + str(4) + " ")
            i += 1
        if irand == 2 and melody_note < 'G': #go up
            melody_melopy += melody_note + " " + chr(ord(melody_note[0])+1) + " "
            w.write(melody_note[:1].lower() + str(4) + " ")
            w.write(chr(ord(melody_note[:1].lower())+1) + str(4) + " ")
            i += 1
        else: #just make it longer
            melody_melopy += '(' + melody_note + ')'
            w.write(melody_note[:1].lower() + str(2) + " ")
            #w.write(melody_note[:1].lower() + "\'" + str(2) + " ")
        if i%4 == 0 and i>0:
            w.write("\n" + "          " )
            melody_count += 1
        i += 1
        if i%4 == 0 and i>0:
            w.write("\n" + "          " )
            melody_count += 1

    w.write("    }\n") #staff closing brackets

    w.write("    \\new Staff\n      {\n") #staff opening brackets
    w.write("        \\key " + temp_key + "\n") #key
    w.write("        \\" + major + "\n") #major/minor
    w.write("        \\clef \"bass\"\n") #treble/bass
    w.write("        \\time 4/4\n") #time signature

    #bass chords
    for bar in track:
        for chord in bar:
            #makes the chord
            lilypitchu = "          "
            note1 = (chord[2][0].name).lower()
            note2 = (chord[2][1].name).lower()
            note3 = (chord[2][2].name).lower()
            if chord == None:
                lilypitchu += r4
            else:
                #now adds the chord
                bass1_melopy += '(' + note1[:1].upper() + ')'
                bass2_melopy += '(' + note2[:1].upper() + ')'
                bass3_melopy += '(' + note3[:1].upper() + ')'
                #for melopy, notes must be uppercase
                lilypitchu += "<" + note1[:1].lower()
                lilypitchu += " " + note2[:1].lower()
                lilypitchu += " " + note3[:1].lower() + ">" + str(bass_length)
            w.write(lilypitchu + "\n")

    w.write("    } >>\n") #staff closing brackets
    w.write("}") #closing brackets

#plays music
with open('D:/Annie/Code/pictoMelody/togetherCodefest/' + filename_melopy,'w') as f:
    f.write(melody_melopy)
    f.write("\n&&&\n")
    f.write(bass1_melopy)
    f.write("\n&&&\n")
    f.write(bass2_melopy)
    f.write("\n&&&\n")
    f.write(bass3_melopy)

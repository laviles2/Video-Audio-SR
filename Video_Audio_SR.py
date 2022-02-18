############################################
#
#                MAC ALERT!
#
############################################

#Make sure you have the following items installed in your computer:
#1. Install Xcode type the following command in your computer terminal:

# xcode-select --install

#2. Instal Home brew:

#  INFO: https://docs.brew.sh/Installation#unattended-installation
#  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

#3. install portaudio using your computers terminal:

#  brew install portaudio

#4.  Install PyAudio using your terminal:

#  pip3 install pyaudio

# OR

# pip install pyaudio

#%. Install moviepy using this command in hte PyCharm Terminal:

# conda install -c conda-forge moviepy


############################################
#
#           SPEECH RECOGNITION
#
############################################
# install Speech Recognition using terminal:

#conda install -c conda-forge speechrecognition


#Import SR using:

import speech_recognition as sr

#Make sure you have an audio file in the current directory that contains English speech
filename = "data/16-122828-0002.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
     #listen for the data (load audio to memory)
    audio_data = r.record(source)
     #recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
#RESULT:
#I believe you're just talking nonsense

##########################
## LARGE AUDIO FILES #####
##########################

# importing libraries
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text

# FILE
path = "data/7601-291468-0006.wav"
print("\nFull text:", get_large_audio_transcription(path))

# MICROPHONE AS INPUT:
#with sr.Microphone() as source:
    # read the audio data from the default microphone
    #audio_data = r.record(source, duration=5)
   # print("Recognizing...")
    # convert speech to text
    #text = r.recognize_google(audio_data)
    #print(text)

# You can also use the offset parameter in the record()
# function to start recording after offset seconds.

#LOTE

#Also, you can recognize different languages by passing language parameter
# to the recognize_google() function. For instance, if you want to recognize
# Spanish speech, you would use:

#text = r.recognize_google(audio_data, language="es-ES")

#More Info: https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134

#PRACTICE (LOTE):
#Select a small audio file of the language you work with make sure it is short:

#Fill in Libraries:


#Set file and recognizer:


#Read file and print result:



############################################
#
#           VID to AUD to TXT
#
############################################


import speech_recognition as sr
import moviepy.editor as mp

#conversion using MoviePy library:
#***convert it to .wav format***

clip = mp.VideoFileClip(r"data/Pokemon_Theme_Song.mp4")

clip.audio.write_audiofile(r"data/Pokemon_ENG.wav")

#Now onto SR

r = sr.Recognizer()

#Import file
audio = sr.AudioFile("data/Pokemon_ENG.wav")

#audio to TXT

with audio as source:
  audio_file = r.record(source)
texto = r.recognize_google(audio_file)



# exporting the result
with open('recognized.txt',mode ='w') as file:
   file.write("Recognized Speech:")
   file.write("\n")
   file.write(texto)
   print("ready!")

#PRACTICE (LOTE):

#Set Libraries

#Set up convertion and format for Audio FIle

#Initiate Speech Recognition and set file


#Write convertion commnads from WAV to TXT


# Export Result :)



##############################################
#
#              YOU   DID   IT  !
#
##############################################







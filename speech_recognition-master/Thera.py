import speech_recognition as sr
import pyaudio
import wave
import pygame
from threading import Thread
from moviepy.editor import VideoFileClip



def func1():
    pygame.display.set_caption('My video!')

    clip = VideoFileClip('voronoi.mp4')
    clip.preview()
    pygame.quit()


def func2():

    chunk = 1024
    wf = wave.open('DR.wav', 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)
    data = wf.readframes(chunk)

    while len(data) > 3:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()

    p.terminate()

def func3():
    pygame.display.set_caption('My video!')

    clip = VideoFileClip('voronoi.mp4')
    clip.preview()
    pygame.quit()


def func4():

    chunk = 1024
    wf = wave.open('CBT.wav', 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)
    data = wf.readframes(chunk)

    while len(data) > 3:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()

    p.terminate()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:

    #Hello  Message from audio

    chunk = 1024
    wf = wave.open('Hello.wav', 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)
    data = wf.readframes(chunk)

    while len(data) > 3:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()

    p.terminate()

    # Starts Listening

    r.adjust_for_ambient_noise(source)  # adapt to the noise
    while True:
        print("Inside loop")
        audio = r.listen(source)

    # recognize speech using Google
        try:
            input = r.recognize_google(audio)

            # Run Video and Audio

            if (input == "I feel stressed"):

                thread = Thread(target=func1)
                thread.start()

                thread2 = Thread(target=func2())
                thread2.start()

                thread.join()
                thread2.join()
                print("thread finished...exiting")

            # If Anxious

            if (input == "I feel happy"):

                thread = Thread(target=func3)
                thread.start()

                thread2 = Thread(target=func4())
                thread2.start()

                thread.join()
                thread2.join()
                print("thread finished...exiting")

        except:

            # Sorry Audio Message if it doesnt understands.

            chunk = 1024
            wf = wave.open('Sorry.wav', 'rb')
            p = pyaudio.PyAudio()

            stream = p.open(
                format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
            data = wf.readframes(chunk)

            while len(data) > 3:
                stream.write(data)
                data = wf.readframes(chunk)

            stream.close()
            p.terminate()
import speech_recognition as sr
import pyaudio
import wave

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

    #Starts Listening

    r.adjust_for_ambient_noise(source) #adapt to the noise
    while True:
        print("Inside loop")
        audio = r.listen(source)

        # recognize speech using Google
        try:
            input = r.recognize_google(audio)

            if(input == "I feel stressed"):
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

            if (input == "I feel anxious"):
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
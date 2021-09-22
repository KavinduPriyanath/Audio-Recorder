import pyaudio
import wave
import time

#Marking the starting time
start_time = time.time()

#Marking the elapsed time
elapsed_time = 0

#Output filename
filename = "Recording.wav"

#Number of frames the signals are split into
chunk = 1024

#sample format
FORMAT = pyaudio.paInt16

#Each frame has 2 samples, 1 for mono and 2 for stereo
channel = 1

#Sampling Rate, Number of frames per seconds
sample_rate = 44100

#Defining PyAudio object
p = pyaudio.PyAudio()

#Open stream object as input & output
stream = p.open(format=FORMAT,
                channels=channel,
                rate=sample_rate,
                input=True,             #Actually sending sound into the stream,or we are trying to record something
                output=True,            
                frames_per_buffer=chunk)
frames = []

choice = int(input("Your choice: "))

if choice == 1:
    record_seconds = int(input("Time you want to record in seconds : "))
    print("Recording in progress...")
    while record_seconds >= elapsed_time:
        current_time = time.time()
        elapsed_time = current_time - start_time
        data = stream.read(chunk)
        frames .append(data)
    print("Finished recording")
elif choice == 2:
    try:
        while True:
            print("Recording in progress...")
            print("Ctrl+C to terminate")
            data = stream.read(chunk)
            frames .append(data)
    except KeyboardInterrupt:
        print("Finished recording")


# stop and close stream
stream.stop_stream()
stream.close()

# terminate pyaudio object
p.terminate()

# save audio file
# open the file in 'write bytes' mode
wf = wave.open(filename, "wb")

# set the channels
wf.setnchannels(channel)

# set the sample format
wf.setsampwidth(p.get_sample_size(FORMAT))

# set the sample rate
wf.setframerate(sample_rate)

# write the frames as bytes
wf.writeframes(b"".join(frames))

# close the file
wf.close()
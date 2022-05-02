import pyaudio
import wave
import numpy

filename = 'test_audio.wav'

chunk = 1024  

wf = wave.open(filename, 'rb')

def audio_callback(indata):
   vol = int(numpy.linalg.norm(indata)/0.5)
   print(vol)

p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

data = wf.readframes(chunk)

while data != '':
    stream.write(data)
    data = wf.readframes(chunk)
    data_s16 = numpy.frombuffer(data, dtype=numpy.int16, count=len(data)//2, offset=0)
    float_data = data_s16 * 0.5**15
    audio_callback(float_data)

stream.close()
p.terminate()

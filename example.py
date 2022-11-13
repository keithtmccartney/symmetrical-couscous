import deepspeech as ds
from IPython.display import display, Audio
import numpy as np
from pydub import AudioSegment
from youtube_dl import YoutubeDL

url ='https://www.youtube.com/watch?v=88WHn6hbMj8'

options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'prefer_ffmpeg': True,
    'keepvideo': False,
    'outtmpl':'audio.%(ext)s'
}

model_path = 'deepspeech-0.9.3-models.tflite'

file = 'audio.wav'

model = ds.Model(model_path)

start = 0

end = 10

channels = 1

rate = 16000

with YoutubeDL(options) as ydl:
    ydl.download([url])

class GetAudio():
    def __init__(self, file=None, channels=1, rate=16000):
        self.channels = channels

        self.rate = rate

        if file is not None:
            self.segment = AudioSegment.from_file(file)

            self.segment = self.segment.set_frame_rate(self.rate)

            self.segment = self.segment.set_channels(self.channels)

    def getSegments(self):
        return self.segment

    def getSegment(self, start, end):
        if self.segment is not None:
            s = start*1000

            e = end*1000

        return self.segment[s:e]

audio = GetAudio(file, channels=channels, rate=rate)

data = audio.getSegment(start, end).get_array_of_samples()

segment = np.array(data, dtype=np.int16)

display(Audio(segment, rate=rate))

stt = model.stt(data)

print(stt)

stream = model.createStream()

segments = audio.getSegments()

buffer = len(segments)

start_offset = 0

batch = 2**11

text = ''

while start_offset < buffer:
    end_offset = start_offset + batch

    chunk = segments[start_offset:end_offset]

    chunk = chunk.get_array_of_samples()

    data = np.frombuffer(chunk, dtype=np.int16)

    stream.feedAudioContent(data)

    text = stream.intermediateDecode()

    print(text)

    start_offset = end_offset

stream.freeStream()

from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("video9/video9.wav", "wav")
chunk_length_ms = 10000  # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms)  # Make chunks of one sec

# Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = "video9/video9-{0}.wav".format(i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")

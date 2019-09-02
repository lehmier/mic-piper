import pyaudio
import signal
import sys

"""
Simple script for piping mic audio into headphones.
Heavily borrowed from the PyAudio "Wire" example:
    https://people.csail.mit.edu/hubert/pyaudio/#docs

Setup:
    brew install portaudio
    pip3 install pyaudio

Run:
    python3 mic_piper.py
"""

def setup_signal_handler(audio, stream):
    """
    Create a signal handler for Control-C.

    The handler stops and closes the stream,
    terminates PyAudio, and exists.
    """
    def signal_handler(sig, frame):
        print("\nStopping playback.")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

def do_loopback(stream, chunk):
    """
    Indefinitely loop while reading audio from the input
    stream and piping it directly into the output streeam.
    """

    print("Starting playback. Press Ctrl+C to exit.")
    while True:
        mic_audio = stream.read(chunk, exception_on_overflow=False)
        stream.write(mic_audio, chunk, exception_on_underflow=False)

def main():
    """
    Do the things
    """

    # Settings and such
    CHUNK = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    WIDTH = 2
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10

    # Build an audio I/O stream  
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)

    # Slap together a Ctrl-C signal handler
    setup_signal_handler(p, stream)

    # Pipe mic data into headphones
    do_loopback(stream, CHUNK)

if __name__ == '__main__':
    main()
# mic-piper
Pipe the input audio from a microphone into headphones

## Setup

This project uses PortAudio audio I/O library. (http://www.portaudio.com/)

`brew install portaudio`

PyAudio is used for the Python interface into PortAudio (https://pypi.org/project/PyAudio/)

`pip3 install pyaudio`

## Running

`python3 mic_piper.py [chunk]`

Simply run mic_piper.py to start piping that audio and hearing yourself speak.

Optionally, you can specify a chunk value. Chunk  is the number of frames into which the audio input is split before piping. By default, chunk=1, so you should be able to hear yourself immediately. Increase the chunk value to insert a delay in the loop. 

## Warning!

Before using this tool, be absolutely certain that you actually have headphones connected and that your system is properly configured to play audio through them. Running your microphone input back through your default speakers and then back into the microphone will create startlingly terrifying feedback loop emulating the sounds of end times. You have been warned.
# symmetrical-couscous
[Python] Mozilla DeepSearch

## Project DeepSpeech

[DeepSpeech](https://github.com/mozilla/DeepSpeech).

## Notes

Consider upgrading the pip version via the (C:\Python39) `python.exe -m pip install --upgrade pip` command.

Install the referenced libraries: `pip install -r requirements.txt`.

This example makes use of a YouTube downloader that transcribes the audio files into text and will require [FFmpeg](https://ffmpeg.org/download.html) to perform these audio tasks; you can install FFmpeg quite easily with [Chocolatey](https://chocolatey.org/install): `choco install ffmpeg`.

Wget - `wget` - is a Linux command to download a file, an equivalent command can be used on Windows but a personal preference the [wget](https://pypi.org/project/wget/) Python package - `pip install wget`; on installing the package we need to then download the DeepSpeak 'tflite' model for this example: `python -m wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.tflite`, keep this model alongside the same location as the example.py file.

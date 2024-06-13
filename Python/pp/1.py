import moviepy.editor
from pathlib import Path

videoFile = Path('[Free for profit] 2010 pop x Kesha x Hyperpop type beat - _Price_ (prod. Aki).mp4')

video = moviepy.editor.VideoFileClip(f'{videoFile}')
audio = video.audio
audio.write_audiofile(f'{videoFile.stem}.mp3')

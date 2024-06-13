import moviepy.editor
from pathlib import Path

videoFile = Path('file/[Free for profit] 2010 pop x Kesha x Hyperpop type beat - _Price_ (prod. Aki).mp4')

video = moviepy.editor.VideoFileClip(f'{videoFile}')
audio = video.audio
audio.write_audiofile(f'file/{videoFile.stem}.mp3')

import moviepy.editor

video = moviepy.editor.VideoFileClip('file/[Free for profit] 2010 pop x Kesha x Hyperpop type beat - _Price_ (prod. Aki).mp4')
audio = video.audio
audio.write_audiofile('file/[Free for profit] 2010 pop x Kesha x Hyperpop type beat - _Price_ (prod. Aki).mp3')

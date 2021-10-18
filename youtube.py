import youtube_dl


print("Colocar o link de uma playlist ou o nome de uma musica do youtube")
url = input()

ydl_opts = {
        'format' : 'bestaudio/best',
        'keepvideo': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
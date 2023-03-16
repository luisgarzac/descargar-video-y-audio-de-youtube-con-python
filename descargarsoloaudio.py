# Descargaremos solo el audio de un video de youtube
from pytube import YouTube

link = 'https://www.youtube.com/watch?v=ITC5nx2XpbU' # Escribe el link del video de youtube
yt = YouTube(link) # Creamos el objeto 
video = yt.streams.get_audio_only('mp4') # Descargamos el audio en formato mp4 (default)
video.download() # Por default se descarga en la carpeta que te encuentres en la terminal
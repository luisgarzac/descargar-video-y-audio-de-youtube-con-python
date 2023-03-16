# Descargaremos un video de youtube con su mayor resolución posible
from pytube import YouTube

link = 'https://www.youtube.com/watch?v=ITC5nx2XpbU' # Escribe el link del video de youtube
yt = YouTube(link) # Creamos el objeto 
video = yt.streams.get_highest_resolution() # get_highest_resolution() -- > Mayor resolución (mp4)
video.download() # Por default se descarga en la carpeta que te encuentres en la terminal

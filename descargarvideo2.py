# Descargaremos un video de youtube con diferentes resoluciones
from pytube import YouTube

link = 'https://youtu.be/ITC5nx2XpbU' # Escribe el link del video de youtube
yt = YouTube(link) # Creamos el objeto 
# Puedes cambiar la resolución deseada: 720p, 480p, 360p, 240p, 144p
video = yt.streams.get_by_resolution("360p")
# Con filename podemos personalizar el nombre del video y su formato
video.download(filename = "resoluciones" + '.mp4') # Por default se descarga en la carpeta que te encuentres en la terminal
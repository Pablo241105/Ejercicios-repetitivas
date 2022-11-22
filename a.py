from pytube import YouTube
from pytube import Playlist


def imprimirHola(nombre:str, apellido:str):
    print("Hola", nombre, apellido)


def sumarDosNumeros(num1:int, num2:int):
    #print("La suma es", num1+num2)
    return num1+num2


def descargaCancion(url:str):
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()

def descargarLista(url:str):
    playlist = Playlist(url)

    for cancion in playlist.videos:
        print("Descargando cancion: ", cancion.title)
        cancion.streams.get_audio_only().download("canciones/")
        print("****************\n")

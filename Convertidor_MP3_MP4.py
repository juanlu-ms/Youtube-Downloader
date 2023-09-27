import os
import pathlib
import shutil
import moviepy.editor as mp

def Convertir (carpeta):
    with os.scandir(carpeta) as ficheros:
        for fichero in ficheros:
            path = pathlib.Path(fichero.path)
            if path.suffix == ".mp4":
                clip = mp.VideoFileClip(fichero.path)
                clip.audio.write_audiofile(f'{path.stem}.mp3', bitrate="320k")
                shutil.move(f'{path.stem}.mp3', 'C:/Users/juanl/OneDrive/Música')
    print("Se han convertido los archivos :")
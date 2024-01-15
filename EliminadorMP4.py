import os
import pathlib
from Rutas import RUTA_MÚSICA

with os.scandir(RUTA_MÚSICA) as ficheros:
    for fichero in ficheros:
        path = pathlib.Path(fichero.path)
        if path.suffix == ".mp4":
            os.remove(fichero.path)
print("Se han eliminado los archivos :)")

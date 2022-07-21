import shutil
import os

def revisaDir(ruta):
    if os.path.exists(ruta):
        if os.path.isdir(ruta):
            return os.listdir(ruta)
    return False
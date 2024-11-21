import subprocess
import os
from pathlib import Path
import os.path
from os import path


# Dato il path di un file lo compila in .pdf mediante il comando 'pdflatex'
def compile(dir_path, file_path):
    try:
        with open(f"compilation.log", "a") as log_file:
            log_file.write("------------------------------------------------------------------------------------------------------")
            subprocess.run(["pdflatex", file_path], cwd=dir_path, check=True, stdout=log_file, stderr=log_file)
        #print(f"{file_path} compilato con successo!")
    except subprocess.CalledProcessError:
        with open(f"errors.log", "w") as test:
            test.write(f"Errore nella compilazione di {file_path}!")


# Cancellazione log di compilazione e log degli errori
os.remove("compilation.log")
if (path.exists("errors.log")):
    os.remove("errors.log")

# Vista riscorsiva della cartella corrente per individuare ogni file .tex
for cartella, sottocartelle, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".tex"):
            # Usa libreria Path per creare oggetto path attraverso concatenazione di cartella e file
            file_path = Path(cartella) / file 
            dir_path = Path(cartella)
            # Traduce path in un formato adatto all'OS is uso
            file_path = file_path.as_posix()
            dir_path = dir_path.as_posix()
            compile(dir_path, file_path)
            compile(dir_path, file_path)
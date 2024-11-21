import subprocess
import os
from pathlib import Path


# Dato il path di un file lo compila in .pdf mediante il comando 'pdflatex'
def compile(dir_path, file_path):
    try:
        with open(f"{file_path}.logs", "w") as log_file:
            subprocess.run(["pdflatex", file_path], cwd=dir_path, check=True, stdout=log_file, stderr=log_file)
        #print(f"{file_path} compilato con successo!")
    except subprocess.CalledProcessError:
        print(f"Errore nella compilazione di {file_path}!")


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
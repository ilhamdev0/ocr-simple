import os
from pathlib import Path
 
input_path = "input/"
output_path = "output/"
ekstensi_valid = (".jpg",".png")


def clear_output_folder():
    [f.unlink() for f in Path(output_path).glob("*") if f.is_file()]

def _filewriter(outputfile, isi):
    with open(f"{output_path}{outputfile}.txt", "w") as file:
        # convert list menjadi baris
        for i in isi:
            file.writelines(f"{i}\n")

def loader(logic):
    for file in os.listdir(input_path):
        if file.endswith(ekstensi_valid):
            teks = logic(f'{input_path}{file}')
            _filewriter(file, teks)
            
            print(f"File \"{file}\" telah diproses")

import easyocr

def proses(file):
    reader = easyocr.Reader(['id'], gpu=False, verbose=False)
    hasil = reader.readtext(
        file,
        detail=0,
        batch_size=6,
        workers=1,
        paragraph=True    
    )

    return hasil
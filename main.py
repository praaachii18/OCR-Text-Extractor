from fastapi import FastAPI, UploadFile, File
import easyocr
import numpy as np
from PIL import Image
import io

app = FastAPI()

reader = easyocr.Reader(['en'])

@app.get("/")
def home():
    return {"message": "OCR API Running"}

@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):

    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")
    image_np = np.array(image)

    results = reader.readtext(image_np)

    text = " ".join([res[1] for res in results])

    return {"text": text}
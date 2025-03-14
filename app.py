import uvicorn
from fastapi import FastAPI
import qr_code.qr_code_generator as imp
from fastapi.responses import StreamingResponse
import segno
import io

app = FastAPI()

@app.get('/hello')
def hello():
    return {"Hello":"World"}

@app.get('/qrcode/{url_param}')
async def generateQrforUrl(url_param: str):
    stream_io = imp.generateRawQrCode(url_param)
    return StreamingResponse(stream_io, media_type="image/png")

@app.get("/qrcode/download")
async def download_qr(data: str = "Hello, World!"):
    qr = segno.make(data)  # Use user-provided text
    img_io = io.BytesIO()
    qr.save(img_io, kind="png")
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/png", headers={"Content-Disposition": f"attachment; filename=qrcode.png"})

if __name__ == "__main__":
   uvicorn.run(app)
   
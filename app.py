import uvicorn
from fastapi import FastAPI
import qr_code.qr_code_generator as imp
from fastapi.responses import StreamingResponse
import segno
import io
from pydantic import BaseModel
from gen_ai.agent_client import chatResponse
from gen_ai.constant import GEMMA3_1B


class ChatBody(BaseModel):
    role: str
    content: str

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
    return StreamingResponse(img_io, media_type="image/png", 
                             headers={"Content-Disposition": f"attachment; filename=qrcode.png"})


@app.post('/chat')
def getChatResponse(req:ChatBody):
    return chatResponse(req.__dict__, GEMMA3_1B)

    return None
if __name__ == "__main__":
   uvicorn.run(app)
   
from typing import Union, Annotated

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse, Response, StreamingResponse
from starlette import status

from pydantic import BaseModel

from pydub import AudioSegment

import io

app = FastAPI()


@app.post("/")
def read_root(file: UploadFile):

    filenameend = file.filename.split('.').pop()
    if filenameend != 'wav':
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="File must be wav.")

    if file.size > 50000000:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="File too large. Cannot be greater than 50mb.")

    # Read the audio file
    sound = AudioSegment.from_file(file.file, format="wav")
    # Export to bytes
    output = io.BytesIO()
    sound.export(output, format="mp3")

    # New file name
    newfilename = file.filename.replace('.wav', '')

    # Return the response
    return Response(content=output.read(), media_type="audio/mp3", headers={"Content-Disposition": f'attachment; filename="{newfilename}.mp3"'})

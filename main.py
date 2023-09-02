# %%
from fastapi import FastAPI,Request
from fastapi import FastAPI, UploadFile, File,Request
from fastapi.responses import *
import uvicorn
import get_sarathi
import requests
import os
import io
from PIL import Image
from fastapi.responses import StreamingResponse
import json
from bs4 import BeautifulSoup

# %%
from fastapi import FastAPI

app = FastAPI()

token=get_sarathi.get_cookie()





@app.get("/")
def root():
  f = open("form.html", "r")
  return HTMLResponse(content=f.read(), status_code=200)


@app.get("/get_token")
def return_token():
  return {'token':get_sarathi.get_cookie()['JSESSIONID']}


@app.get("/get_captcha/{id}",responses = {200: {"content": {"image/png": {}}}},response_class=Response)
def return_capcha(id):
  img_path=get_sarathi.get_captcha(id)
  image = Image.open(img_path)
  # create a thumbnail image
  image.thumbnail((100, 100))
  imgio = io.BytesIO()
  image.save(imgio, 'JPEG')
  imgio.seek(0)
  os.remove(img_path)
  return StreamingResponse(content=imgio, media_type="image/jpeg")


@app.get("/get_data/{id}/")
def return_data(id=False,dlno=False,dob=False,capcha=False):
  if id and dlno and dob and capcha:
    info1=get_sarathi.getLastEndorsedRtoDLserReq(id,dlno,dob,capcha)
    info1_d=json.loads(info1)
    if(info1_d[1]=='OK'):
      csrf_token=get_sarathi.get_sarathi_csrf_token(id)
      if(csrf_token):
        csrf_token=get_sarathi.get_sarathi_csrf_token(id)
        info2=get_sarathi.get_submitter_result(id,dlno,dob,capcha,csrf_token,info1_d)
        return info2
      else:
        return {'status':False,'info':'Retry The Request. Get Trouble to Proccess Csrf Token'}
    else:
      try:
        return {'status':False,'info':info1_d[1]}
      except:
        return {'status':False,'info':'Capcha Not Correct'}
  else:
    return {'status':False,'info':'Parameters Missing'}



if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)

# %%

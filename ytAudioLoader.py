
from pytube import YouTube
# import argparse, sys
import whisper
from datetime import datetime
import os

link=os.getenv("link")
model=os.getenv("model")
device=os.getenv('device')

if model=='None':
  print('''Selected model: base (default)
  You can set env variable 'model' == tiny | base | small | medium | large | large-v2  | large-v3
  or their .en equivalents''')
  model='base'

now = datetime.now()

def recognizeAudio(audiofile):
  try:   
    print('Start recognizing: {} model'.format(model))
    AIModel = whisper.load_model(model)
    AIModel.cpu()
    if device == 'cuda':
      AIModel.cuda()
    result = AIModel.transcribe(audiofile, verbose=False)
    date_time = now.strftime("%Y%m%d_%H_%M")
    outputFile = '{}_{}_{}.txt'.format(date_time, device, model)
    with open('/app/output/{}'.format(outputFile), 'w', encoding="utf-8") as f:
      f.write(result["text"])
    print('Finish recognizing: successfuly')
    print('Output filename: ./output/{}'.format(outputFile))
  except BaseException as exc:
    print(exc)
    print('BaseException above was caught during recognizing audiofile')

def downloadAudiofile(link):
  if link=='None':
    return '''
link variable is not provided
  You must provide it as environment variable
  In docker run cli use -e link="https://youtube.com/........"'''
  else:
    try:
      print('Start download: {}'.format(link))
      yt = YouTube(f"{link}")
      yt.streams.filter(type='audio').order_by('abr').desc().first().download(output_path='/app', filename='audiofile')
      if os.path.exists("/app/audiofile"):
        print('Finish download: successfuly')
        return 0
      else:
        return '''
Something went wrong during downloading
  Maybe link is broken, link must be https://youtube.com/........'''
    except BaseException as exc:
      print(exc)
      return 'BaseException above was caught during downloading audiofile'

def start():
  audioRes = downloadAudiofile(link)
  if audioRes == 0:
    if os.path.exists("/app/audiofile"):
      audiofile = whisper.load_audio('/app/audiofile')
      recognizeAudio(audiofile)
    else:
      print('/app/audiofile does not exist')
  else:
    print(audioRes)
  
start()
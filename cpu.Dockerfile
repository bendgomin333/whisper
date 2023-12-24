FROM python:3.10-slim
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y ffmpeg git && \
  pip install -U openai-whisper && \
  pip install pytube

ENV model=None
ENV link=None
ENV device=cpu

COPY . /app

ENTRYPOINT [ "python", "/app/ytAudioLoader.py" ]
CMD [""]
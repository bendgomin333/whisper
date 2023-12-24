FROM nvidia/cuda:12.3.1-base-ubuntu20.04

ENV model=None
ENV link=None
ENV device=cuda
ENV DEBIAN_FRONTEND=noninteractive

# install python3.10 from source (takes more time)
# RUN apt-get install wget -y
# WORKDIR /usr/src
# RUN wget https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz
# RUN tar xzf Python-3.10.13.tgz
# WORKDIR /usr/src/Python-3.10.13
# RUN ./configure --enable-optimizations
# RUN make altinstall

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:deadsnakes/ppa && \
  apt-get update
RUN apt-get install -y \
  python3.10 \
  python3.10-distutils \
  ffmpeg \
  python3-pip \
  curl

# updating pip to make it work with python 3.10
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

# create links for python and pip
RUN ln -s -f /usr/bin/python3.10 /usr/bin/python3 && \
  ln -s -f /usr/bin/python3.10 /usr/bin/python && \
  ln -s -f /usr/bin/pip3 /usr/bin/pip

RUN pip3 install -U \
  openai-whisper \
  torchaudio \
  torchvision \
  pytube

COPY . /app

# RUN python /app/ytAudioLoader.py --link=${link}
ENTRYPOINT [ "python", "/app/ytAudioLoader.py" ]
CMD [""]
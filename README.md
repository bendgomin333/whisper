## How to build images?
Run `docker pull bendgomin333/whisper:cpu` for cpu device, `docker pull bendgomin333/whisper:gpu` for gpu device

Or you can build image from Dockerfile
1. clone repository
2. cd to repository
3. run `docker build -t imagename:tag -f gpu* .` for cuda device, `docker build -t imagename:tag -f cpu* .` for cpu device

> Builded image takes about 10GB

## How to run container?
run `sudo docker run --rm -v "/absolute/local/path/to/models/folder":/root/.cache/whisper -v "/absolute/local/path/to/output/folder":"/app/output" -it --gpus all -e model=tiny -e link="https://www.youtube.com/watch.........." bendgomin333/whisper:gpu`<br />
**required flags:**
`-v "/absolute/local/path/to/models/folder":/root/.cache/whisper`: bind local folder to image folder with cached models. This allows you to store models without downloading every time you create a container<br />
`-v "/absolute/local/path/to/output/folder":"/app/output"`: bind local folder to image folder with output files<br />
`-e link="https://www.youtube.com/watch.........."`: link to yt video<br />
`bendgomin333/whisper:gpu`: image name (tag could be `gpu` for CUDA device or `cpu` for CPU device)<br />
`--gpus all`: Must be provided when using CUDA device. Allows you to use the GPU inside the image (`nvidia-container-toolkit` package must be installed on the host machine)<br />

**optional:**

`--rm`: remove container after recognizing (recommended)<br />
`-e model=model_name`: choosen whisper model. Could be tiny|base|small|medium|large|large-v2|large-v3 or their `.en` equivalents (default=`base`)
`-it`: interactive mode for better cli outputs<br />

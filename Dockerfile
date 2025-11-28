FROM pytorch/pytorch:2.0.0-cuda11.8-cudnn8-runtime

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install moviepy whisperx transformers accelerate opencv-python

COPY predict.py /src/predict.py

WORKDIR /src

CMD ["python3", "predict.py"]

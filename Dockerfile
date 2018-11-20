FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

# Install pytorch and fastai
RUN pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html
RUN pip install fastai

# Install starlette and uvicorn
RUN pip install flask gevent requests

ADD bears.py bears.py
ADD data data

# Run it once to trigger resnet download
# RUN python bears.py

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["bears.py"]

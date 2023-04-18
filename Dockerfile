FROM python:3.11

WORKDIR /sage-challenge

COPY ./requirements.txt /sage-challenge/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /sage-challenge/requirements.txt

COPY ./src /sage-challenge/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

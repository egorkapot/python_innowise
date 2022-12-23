FROM python:3.10.6

COPY . /Innowise_Python_Task1

WORKDIR /Innowise_Python_Task1

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]

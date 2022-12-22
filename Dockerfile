FROM python:3.10.6

WORKDIR /home/user/Desktop/

COPY . .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"] 
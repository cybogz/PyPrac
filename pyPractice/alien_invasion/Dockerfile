FROM python:3.12

WORKDIR /alien_invasion

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "alien_invasion.py"]
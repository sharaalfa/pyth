FROM python:2.7.11-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
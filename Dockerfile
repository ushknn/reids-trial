FROM python:3.12
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py

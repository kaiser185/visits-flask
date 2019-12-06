# our base image
FROM python:3.7

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install pymongo Flask-Cors

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

EXPOSE 5000
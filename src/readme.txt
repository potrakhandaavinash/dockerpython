create an redis image and run the image in the docker 
docker run -p 6379:6379 redis
docker run -p 9999:5555 (name of the image)

clear cache
docker system prune -a

FROM python:3.10-bullseye

COPY test.py /

COPY requirements.txt /

RUN pip install -r requirements.txt


CMD [ "python3", "-u", "test.py" ]


------------------------------------------------------------
FROM python:3.10-bullseye

COPY requirements.txt /

WORKDIR /usr/hello
 
COPY requirements.txt /

RUN pip install -r requirements.txt


CMD [ "python3", "-u", "test.py" ]

-------------------------------------------------------------

FROM python:3.10-bullseye

WORKDIR /usr/my

COPY ./ ./

RUN pip install -r requirements.txt

CMD [ "python3", "-u", "test.py" ]


----------------------------------------------------------------

# Dockerfile 
#requirements.txt
#src|
#	|test.py
FROM python:3.10-bullseye

WORKDIR /usr/my/asa/asasas

COPY ./ ./

RUN pip install -r requirements.txt

CMD [ "python3", "-u", "src/test.py" ]


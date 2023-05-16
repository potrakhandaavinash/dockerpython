FROM python:3
COPY test.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "-u", "test.py" ]

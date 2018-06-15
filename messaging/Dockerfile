FROM python:3.5

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY settings.py ./
COPY run.py ./

CMD [ "python", "./run.py" ]

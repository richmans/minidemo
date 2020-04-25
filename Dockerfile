FROM python:3.8.2-buster

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
COPY cloud_manifest.yml /

COPY app.py .
EXPOSE 5000
CMD [ "python", "./app.py" ]
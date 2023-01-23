# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /.
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get -y install git
COPY . .
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

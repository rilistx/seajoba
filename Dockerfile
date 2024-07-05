FROM python:3.12.3

RUN apt-get update || apt-get upgrade

WORKDIR /seajoba

COPY ./commands ./commands
COPY ./core ./core
COPY ./alembic.ini ./alembic.ini
COPY ./bot.py ./bot.py
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]

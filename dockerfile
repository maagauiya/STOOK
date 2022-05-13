FROM python:3
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app

EXPOSE 8000

CMD ["python","manage.py","runserver","manage.py"]
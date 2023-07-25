FROM python:3.12-rc-slim

WORKDIR /code

COPY ./src ./src

# COPY ./requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt


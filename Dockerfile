# pull official base image
FROM python:3.10.6

# set working directory
WORKDIR /test_tasks

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy all files and directories to /test_tasks/ folder
COPY . .

# install packages
RUN pip install --no-cache-dir --upgrade -r requirements.txt
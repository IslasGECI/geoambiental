FROM python:3.7
COPY . /workdir/
WORKDIR /workdir
RUN pip install --requirement requirements.txt

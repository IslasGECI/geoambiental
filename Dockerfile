FROM python:3.8
WORKDIR /workdir
COPY . .
RUN pip install --requirement requirements.txt
CMD make

FROM python:3.9
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    flake8 \
    mutmut==2.* \
    mypy \
    pylint \
    pytest \
    pytest-cov

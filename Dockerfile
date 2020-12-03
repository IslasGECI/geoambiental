FROM python:3.8
WORKDIR /workdir
COPY . .
RUN pip install --requirement requirements.txt
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    flake8 \
    lmfit \
    mutmut \
    numpy \
    pandas \
    pylint \
    pytest-cov \
    pytest==5.0.1 \
    scipy
CMD make

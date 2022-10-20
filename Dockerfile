FROM python:3.10
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    matplotlib \
    mutmut \
    pandas \
    pandas-datareader \
    pylint \
    pydantic \
    pytest \
    pytest-cov \
    rope \
    typer \
    yahooquery

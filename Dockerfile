# IMPORT
FROM python:3.8-slim-buster

# WORKDIR
WORKDIR /code

# COPY requirements.txt
COPY requirements.txt requirements.txt

# INSTALL PIP DEPENDENCIES
RUN pip install -r requirements.txt

# EXPOSE PORT
EXPOSE 8015

# COPY FILE
COPY . ./

# CMD python main.py
CMD ["python3", "auto-api.py"]

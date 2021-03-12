FROM python:3
WORKDIR /usr/src/app

COPY Routerdata.csv .
COPY db_csv.py .

COPY callbacks.py .
COPY layouts.py .
COPY app.py .
COPY assets /usr/src/app/assets 
COPY index.py .
COPY requirements.txt .
EXPOSE 8765
RUN pip install -r requirements.txt

CMD ["python","./index.py"]

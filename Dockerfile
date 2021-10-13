FROM python:3.8

EXPOSE 8000

WORKDIR /eudat/B2SHARE-FAIR
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src .
CMD ["gunicorn", "proxy.app:app", "--bind=0.0.0.0:8000", "-w", "1"]
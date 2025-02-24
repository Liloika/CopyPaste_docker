FROM python:3.13

WORKDIR /app

COPY main.py ./

RUN pip install --no-cache-dir flask==2.2.2

EXPOSE 5000

CMD ["python", "main.py"]

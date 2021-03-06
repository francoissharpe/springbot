FROM python:3.8

WORKDIR /springbot

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["gunicorn", \
            "--workers", "5", \
            "--timeout", "60", \
            "--bind=0.0.0.0:5000", \
            "main:app"]

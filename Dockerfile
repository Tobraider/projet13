FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ARG ARG_DNS_SENTRY=''
ARG ARG_SECRET_KEY=''
ARG DEBUG=''
ARG IPPROD=''

ENV DNS_SENTRY=$ARG_DNS_SENTRY
ENV SECRET_KEY=$ARG_SECRET_KEY
ENV DEBUG=$DEBUG
ENV IPPROD=$IPPROD

RUN python manage.py migrate
RUN python manage.py collectstatic

EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --clear --noinput && python manage.py runserver 0.0.0.0:8000"]
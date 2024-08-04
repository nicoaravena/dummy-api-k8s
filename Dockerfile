ARG APP_VERSION=0.0.0

FROM python:3.10

ENV APP_VERSION=$APP_VERSION
ENV CONFIGS_FOLDER=/etc/dummy.k8s.d
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8

RUN echo "Generating dummy-api-k8s container v${APP_VERSION}"

LABEL description="Dummy API made with FastAPI and with k8s"

WORKDIR /var/opt

RUN mkdir -p /etc/dummy.k8s.d

COPY ./settings.cfg.dist /etc/dummy.k8s.d/settings.cfg.dist

COPY ./requirements.txt /var/opt/requirements.txt

RUN pip install --no-cache-dir -U -r /var/opt/requirements.txt

RUN rm /var/opt/requirements.txt

COPY ./api /var/opt/dummy-api

CMD ["uvicorn", "api.main:app"]

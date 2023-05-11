FROM python:3.10

#RUN apt-get update -qq
#RUN apt-get install python3.10 python3-pip -y --no-install-recommends && rm -rf /var/lib/apt/lists_/*

WORKDIR /ocean

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./bin/docker_entrypoint.sh /docker_entrypoint.sh
COPY ./ /ocean

EXPOSE 8000

CMD ["/docker_entrypoint.sh"]

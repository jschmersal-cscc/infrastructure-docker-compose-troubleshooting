# More Dockerfile commands.  For more reference, see https://docs.docker.com/engine/reference/builder/
FROM alpine

ENV MY_ENV_VAR=foo

RUN mkdir /app
COPY . /app

CMD /app/run-it.sh

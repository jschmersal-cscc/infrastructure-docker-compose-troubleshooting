# Docker Compose

Docker Compose lets you run a suite of containers with specified configurations, all interconnected.

## Prerequisite
Before you can perform this example, you need to install docker compose.  To do so, run the following two commands:
+ `sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
+ `sudo chmod +x /usr/local/bin/docker-compose`

To validate that this works, run `docker-compose --version`.  The output should be similar to this:
```
[jschmersal1@WFIL011 01-basic-compose]$ docker-compose --version
docker-compose version 1.26.2, build eefe0d31
```

## Introduction
This example is a basic python web application.  However, when you're creating even the most simple
web app, you will likely need some type of database for persistence.  In this case we're using Redis, a high performance in-memory database.

To make this application work, you will need to stand up two containers:
* A web app container to run your python code
* A redis container to hold persistent data

## Getting started
First, review the [Dockerfile](Dockerfile), [build.sh](build.sh), [requirements.txt](requirements.txt) and [app.py](app.py) to get an idea of what to expect.

Once you have an idea of what _should_ happen when running your app, check out the [docker-compose.yml](docker-compose.yml).  In that file you have two services defined: `webapp` and `db`

## Running the example
To run the example, first build the docker container for the webapp: `./build.sh`

You should see something like:
```
[jschmersal1@WFIL011 01-basic-compose]$ ./build.sh 
Sending build context to Docker daemon  31.74kB
Step 1/10 : FROM python:3.7-alpine
3.7-alpine: Pulling from library/python
df20fa9351a1: Already exists 
36b3adc4ff6f: Pull complete 
d4f879c74e1d: Pull complete 
6064e23ad526: Pull complete 
2551f262ffbe: Pull complete 
Digest: sha256:afbf56228fee964053a9be2724ce3d946de5ff38b166d97e51faa919591b549e
Status: Downloaded newer image for python:3.7-alpine
 ---> c4d4af4fa7c0
Step 2/10 : ENV FLASK_APP app.py
 ---> Running in 17826482bed4
Removing intermediate container 17826482bed4
 ---> 54b40285e75f
Step 3/10 : ENV FLASK_RUN_HOST 0.0.0.0
 ---> Running in ce8dcb57b896
Removing intermediate container ce8dcb57b896
 ---> 498ffd90a21a
Step 4/10 : RUN apk add --no-cache gcc musl-dev linux-headers
 ---> Running in 6f58001accdf
fetch http://dl-cdn.alpinelinux.org/alpine/v3.12/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.12/community/x86_64/APKINDEX.tar.gz
(1/13) Installing libgcc (9.3.0-r2)
(2/13) Installing libstdc++ (9.3.0-r2)
(3/13) Installing binutils (2.34-r1)
(4/13) Installing gmp (6.2.0-r0)
(5/13) Installing isl (0.18-r0)
(6/13) Installing libgomp (9.3.0-r2)
(7/13) Installing libatomic (9.3.0-r2)
(8/13) Installing libgphobos (9.3.0-r2)
(9/13) Installing mpfr4 (4.0.2-r4)
(10/13) Installing mpc1 (1.1.0-r1)
(11/13) Installing gcc (9.3.0-r2)
(12/13) Installing linux-headers (5.4.5-r1)
(13/13) Installing musl-dev (1.1.24-r9)
Executing busybox-1.31.1-r16.trigger
OK: 153 MiB in 48 packages
Removing intermediate container 6f58001accdf
 ---> 902af9be2f2b
Step 5/10 : RUN mkdir /app
 ---> Running in 4678668ddf52
Removing intermediate container 4678668ddf52
 ---> d6fb51aa5d05
Step 6/10 : WORKDIR /app
 ---> Running in 750b383e752d
Removing intermediate container 750b383e752d
 ---> 80d62cb7c396
Step 7/10 : COPY requirements.txt /app
 ---> 3c98ef126857
Step 8/10 : RUN pip install -r requirements.txt
 ---> Running in bad9246fe2c2
Collecting flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting redis
  Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting click>=5.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1.tar.gz (19 kB)
Building wheels for collected packages: MarkupSafe
  Building wheel for MarkupSafe (setup.py): started
  Building wheel for MarkupSafe (setup.py): finished with status 'done'
  Created wheel for MarkupSafe: filename=MarkupSafe-1.1.1-cp37-cp37m-linux_x86_64.whl size=16912 sha256=491182614879d5c1a59d7f4f191d4dfc2766b743b790a08a902c4d846f598940
  Stored in directory: /root/.cache/pip/wheels/b9/d9/ae/63bf9056b0a22b13ade9f6b9e08187c1bb71c47ef21a8c9924
Successfully built MarkupSafe
Installing collected packages: itsdangerous, Werkzeug, click, MarkupSafe, Jinja2, flask, redis
Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0 redis-3.5.3
Removing intermediate container bad9246fe2c2
 ---> 56d94df07a22
Step 9/10 : COPY . .
 ---> d06fd2b1e6db
Step 10/10 : CMD ["flask", "run"]
 ---> Running in d4615a366de3
Removing intermediate container d4615a366de3
 ---> 4ef867414b93
Successfully built 4ef867414b93
Successfully tagged infra-example-3-1:0.1
```

Now that we have built our `infra-example-3-1:0.1` image, we can run our composition: `docker-compose up -d`

You should see something like:
```
[jschmersal1@WFIL011 01-basic-compose]$ docker-compose up -d
Creating network "01-basic-compose_default" with the default driver
Pulling db (redis:alpine)...
alpine: Pulling from library/redis
df20fa9351a1: Already exists
9b8c029ceab5: Pull complete
e983a1eb737a: Pull complete
660ad543c5fc: Pull complete
823cbe4f5025: Pull complete
e3dd0c30e1c8: Pull complete
Digest: sha256:6972ee00fd35854dd2925904e23cb047faa004df27c62cba842248c7db6bd99d
Status: Downloaded newer image for redis:alpine
Creating 01-basic-compose_db_1     ... done
Creating 01-basic-compose_webapp_1 ... done
```

Run `docker ps` and see what containers are running now:

```
[jschmersal1@WFIL011 01-basic-compose]$ docker ps
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS                    NAMES
33afe6a159ed        redis:alpine            "docker-entrypoint.s…"   4 seconds ago       Up 3 seconds        6379/tcp                 01-basic-compose_db_1
eb983c1a594b        infra-example-3-1:0.1   "flask run"              4 seconds ago       Up 3 seconds        0.0.0.0:8080->5000/tcp   01-basic-compose_webapp_1
```

Notice the naming convention on the docker containers that are created.

Navigate your browser to [http://localhost:8080](http://localhost:8080).  Click the refresh button
a few times.  See the counter change?

Now, stop and remove the containers:
```
[jschmersal1@WFIL011 01-basic-compose]$ docker-compose rm -sf
Stopping 01-basic-compose_db_1     ... done
Stopping 01-basic-compose_webapp_1 ... done
Going to remove 01-basic-compose_db_1, 01-basic-compose_webapp_1
Removing 01-basic-compose_db_1     ... done
Removing 01-basic-compose_webapp_1 ... done
```

Verify they are gone with `docker ps -a`

## In-class example
Now that you have the basic webapp working, let's try to improve your composition.  
Restart your app (`docker-compose up -d`) and go to the homepage again ([http://localhost:8080](http://localhost:8080).  Notice there's a problem here -- the counter reset to 0 when we restarted the application. 

Fix this.  To do so, you will need to mount an external volume to persist the redis data into.  Note from [the redis docker hub page](https://hub.docker.com/_/redis) that redis reads and writes its database data in `/data` inside the contaner.  Also, you can see how to configure volumes in docker compose by reading through the [compose configuration page](https://docs.docker.com/compose/compose-file/#volumes).

Test your fix by running `docker-compose down` and then `docker-compose up -d` a few times.  

_Note:_ this example borrows heavily from https://docs.docker.com/compose/gettingstarted/ (it's
basically a copy).

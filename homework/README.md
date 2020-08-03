# Docker Compose Homework
This week's homework concentrates on Docker Compose.

# Getting Started
[Mediawiki]() is an open source wiki that uses the traditional [LAMP]() stack (`Linux`, `Apache`, 
`MySQL`, and `Php`). Traditionally getting those components installed correctly could be a 
challenge.  Lucky for us, there are docker images already available, including one with the
mediawiki software installed!

Your goal for this lab, is to modify the existing [docker-compose.yml](docker-compose.yml) in this
directory to define a set of services that will create a functional wikimedia application instance.

# Requirements
For this to be successful, your [docker-compose.yml](docker-compose.yml) must meet the following
criteria:

+ You should define two volumes, `db_data` and `mw_data`.  It is acceptable for the volumes to just use the `local` driver.
+ You should define two services, `db` and `mw`.
+ The `db` service should use the `mariadb` image (tagged `10.3`).  [Mariadb](https://mariadb.com/)
 is an open source fork of MySQL because Oracle has taken over the rights to the original MySQL.
+ You will need to define the following environment variables for the `db` service:
  * `MYSQL_ALLOW_EMPTY_PASSWORD` (set to `yes`)
  * `MYSQL_USER` (set to `mw_user`)
  * `MYSQL_PASSWORD` (set to a password of your choice)
  * `MYSQL_DATABASE` (set to `mediawiki_db`)
+ The `db` service should have the `db_data` volume mounted to `/var/lib/mysql` in the container
+ The `mw` service should use the `docker.io/bitnami/mediawiki:1-debian-10` image. [Bitnami](https://bitnami.com/) packages open source applications for easier consumption.  In this case, their docker is much easier to use than the vanilla `mediawiki:stable` docker image, as it goes through the process of doing the basic installation setup.  If we were doing this "for real" we would likely go through the process of tweaking the settings as we desired.
+ The `mw` service should listen on port `9786` on your host (it listens on port `8080` inside the container).
+ You will need to define the following environment variables for the `mw` service:
  * `ALLOW_EMPTY_PASSWORD` (set the same as the corresponding variable in the `db` service)
  * `MEDIAWIKI_DATABASE_USER` (set the same as the corresponding variable in the `db` service)
  * `MEDIAWIKI_DATABASE_PASSWORD` (set the same as the corresponding variable in the `db` service)
  * `MEDIAWIKI_DATABASE_NAME` (set the same as in the `db` service's `MYSQL_DATABASE`)
  * `MEDIAWIKI_HOST` (set to `localhost:9786`) - this is the host name that mediawiki redirects to.
  * `MEDIAWIKI_DATABASE_HOST` (you have to determine what this should be)
  * `MEDIAWIKI_DATABASE_PORT_NUMBER` (set to `3306` - the default mysql port)
+ The `mw` service should have the `mw_data` volume mounted to `/bitnami/mediawiki` in the container

# Hints
A few hopefully helpful hints as you work through this process:

* Start small.  Perhaps just start with the database.  You can check if you can connect to your runnind database by running `docker exec -it <container-name> bash -c "mysql -u <username> -p<password> "`
* If you have things pretty messed up, or have an issue with things not quite working when they did before, you can run `./cleanup.sh`.  _Warning_: that script will blow away _all_ containers, volumes, and networks (not just the ones related to this lab).  Be careful.
* Don't forget that you can look at the logs of your containers.  For instance, I was able to see the logs of my mediawiki container by running `docker logs -f homework_mw_1` (yours should be similar).
* Remember, YAML is finicky.  You can use [this YAML parser](https://yaml-online-parser.appspot.com/) to make sure your YAML is being interpreted the way you _think_ it is.

# Final thoughts
This is a good example, but there are some concerns here.  For instance, is it a good idea to have database users and passwords defined in our [docker-compose.yml](docker-compose.yml)?  Why not?  How would you change your compose yml file to shore things up a bit?

Similarly allowing empty passwords... good practice or not?

What would you change if you needed to have the database content stored using a network storage technique?  Or backed by AWS?  What if prod had a different database storage need than dev?  How would you separate the two? 

This doesn't scale well...  You have one web server and one database server.  How could you go about scaling that to multiple service instances?  Spread across multiple hosts?

These are all just thought exercises.  You don't need to answer them as part of the homework assignment.


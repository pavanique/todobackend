FROM narisp/todobackend-base:latest

MAINTAINER Narisetty Pavan <npavankumar.tech@gmail.com>

# Install python dev/build dependencies
RUN apt-get update && \
	apt-get install -qy python-dev libmysqlclient-dev

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
	pip install wheel --upgrade

#Pip environment  variables (Note: must be set after wheel installation)
ENV WHEELHOSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

#OUTPUT: Build artifacts (Wheels) are output here
VOLUME /wheelhouse

#OUTPUT: TEST reports output are here
VOLUME /reports

#ADD the entry script here 
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

#Set defaults for entry point and command string
ENTRYPOINT ["test.sh"]
CMD ["python", "manage.py", "test", "--noinput"]

COPY src /application
WORKDIR /application
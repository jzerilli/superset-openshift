FROM registry.access.redhat.com/ubi7/python-36:latest
MAINTAINER Zak Hassan <zak.hassan1010@gmail.com>

RUN pip install --default-timeout=1000  --no-cache-dir   superset==0.24.0 click==6.7 pymysql pyhive

RUN fabmanager create-admin --app superset \
  --username admin \
  --firstname admin \
  --lastname admin \
  --email admin@admin.com \
  --password admin

RUN superset db upgrade && \
superset init

EXPOSE 8088
# Start the web server on port 8088, use -p to bind to another port
CMD ["superset","runserver"]

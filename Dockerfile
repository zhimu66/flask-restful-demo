FROM flask-restful-example

VOLUME ["/projects", "/logs"]
CMD sh ./run.sh


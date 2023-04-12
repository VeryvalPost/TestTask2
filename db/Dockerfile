FROM postgres:latest

ENV POSTGRES_DB=postgres
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_NAME=postgres

ADD /init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD ["postgres"]
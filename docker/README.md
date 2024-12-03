# Docker Services for Health App

This directory contains the Docker configurations for the Health App project. Below are the instructions to run the different services: PostgreSQL, Flask, and Airflow.

## Prerequisites

- Docker
- Docker Compose

## Services

### PostgreSQL

1. Navigate to the `docker` directory.
2. Run the following command to start the PostgreSQL service:
```sh
docker-compose up -d postgres
```

To log into the PostgreSQL database instance, run:
```sh
docker exec -it postgres psql -U <username>
```
Replace `<username>` with the PostgreSQL username.

Once logged in, list all databases with:
```sh
\l
```

To list all users, run:
```sh
\du
```

To check tables within a database, connect to the desired database:
```sh
\c <database_name>
```
Replace `<database_name>` with the name of the database you want to connect to.

Then, list all tables in the connected database with:
```sh
\dt
```

### Flask

Run the following command to start the Flask service:
```sh
docker-compose up -d flask
```

To get into the Flask container, run:
```sh
docker exec -it flask /bin/sh
```

If you need to initialize the database, run the following command inside the Flask container:
```sh
flask db init
```

Once inside the container, run the following commands to perform the database migration and upgrade:
```sh
flask db migrate
flask db upgrade
```


### Airflow

1. Ensure the PostgreSQL service is running.
2. Run the following command to start the Airflow service:
```sh
docker-compose up -d airflow
```

## Stopping Services

To stop any of the services, run:
```sh
docker-compose down
```

## Logs

To view the logs for a specific service, use:
```sh
docker-compose logs <service_name>
```
Replace `<service_name>` with `postgres`, `flask`, or `airflow`.

## Additional Information

- Ensure all environment variables required by the services are properly configured in the `.env` file.
- For more detailed configurations, refer to the individual Dockerfiles and `docker-compose.yml`.

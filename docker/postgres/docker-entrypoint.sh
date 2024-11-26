#!/bin/bash
set -e

# Start PostgreSQL in the background to allow initialization
docker-entrypoint.sh postgres &

# Wait for PostgreSQL to fully start
sleep 5

# Create databases and users based on environment variables
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
  CREATE DATABASE ${FLASK_DB};
  CREATE DATABASE ${AIRFLOW_DB};
  CREATE USER ${FLASK_USER} WITH PASSWORD '${FLASK_PASSWORD}';
  CREATE USER ${AIRFLOW_USER} WITH PASSWORD '${AIRFLOW_PASSWORD}';
  GRANT ALL PRIVILEGES ON DATABASE ${FLASK_DB} TO ${FLASK_USER};
  GRANT ALL PRIVILEGES ON DATABASE ${AIRFLOW_DB} TO ${AIRFLOW_USER};
EOSQL

# Wait for PostgreSQL to exit
wait

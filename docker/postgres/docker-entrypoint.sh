#!/bin/bash
set -e

# Start PostgreSQL in the background to allow initialization
docker-entrypoint.sh postgres &

# Wait for PostgreSQL to fully start
until pg_isready --username="$POSTGRES_USER"; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

# Create databases and users based on environment variables
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  -- Create users with passwords
  CREATE USER "${FLASK_USER}" WITH PASSWORD '${FLASK_PASSWORD}';
  CREATE USER "${AIRFLOW_USER}" WITH PASSWORD '${AIRFLOW_PASSWORD}';

  -- Create the databases and set the owners
  CREATE DATABASE "${FLASK_DB}" OWNER "${FLASK_USER}";
  CREATE DATABASE "${AIRFLOW_DB}" OWNER "${AIRFLOW_USER}";

  -- Airflow user permissions (data manipulation only)
  GRANT CONNECT ON DATABASE "${FLASK_DB}" TO "${AIRFLOW_USER}";
  GRANT USAGE ON SCHEMA public TO "${AIRFLOW_USER}";
  GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO "${AIRFLOW_USER}";
  ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO "${AIRFLOW_USER}";
  GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO "${AIRFLOW_USER}";
  ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO "${AIRFLOW_USER}";
EOSQL

# Wait for PostgreSQL to exit
wait

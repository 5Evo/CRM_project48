CREATE DATABASE crm_db;
CREATE USER crm_user with NOSUPERUSER PASSWORD 'superuser';
GRANT ALL PRIVILEGES ON DATABASE crm_db TO crm_user;

ALTER ROLE crm_user SET CLIENT_ENCODING TO 'UTF8';
ALTER ROLE crm_user SET default_transaction_isolation TO 'READ COMMITTED';
ALTER ROLE crm_user SET TIME ZONE 'Asia/Yekaterinburg';

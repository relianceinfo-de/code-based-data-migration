# code-based-data-migration
Data Migration Tool for MySQL to Azure SQL Server and PostgreSQL

This project provides a tool for migrating data from a MySQL database to both Azure SQL Server and PostgreSQL databases. It uses environment variables for secure database credential management and connects to the databases via Python libraries. This setup facilitates data transfer, particularly for data synchronization or integration tasks between different database environments.

# Features
Environment Variable Management: Uses .env files to securely store and load database credentials.
MySQL Connection: Connects to MySQL using pymysql and retrieves data from a specified table.
Azure SQL Server and PostgreSQL Connections: Establishes connections to both Azure SQL Server and PostgreSQL using pyodbc and psycopg2 libraries.

# Data Transfer Automation: Automates the entire migration process:
Fetches data from MySQL.
Creates and defines the schema in the destination database tables.
Inserts data into the destination tables.
Error Handling and Connection Management: Closes all connections upon task completion to prevent memory leaks and ensure reliable resource management.

# Requirements
Python Libraries: pymysql, pyodbc, psycopg2, dotenv
Database Drivers: ODBC Driver 17 for SQL Server (for Azure SQL Server), PostgreSQL, and MySQL drivers
Environment Variables: .env file with MySQL, Azure SQL Server, and PostgreSQL connection details

# Environment Variables
Create a .env file with the following variables:
# MySQL Database
MYSQL_HOST=<your_mysql_host>
MYSQL_USER=<your_mysql_user>
MYSQL_PASSWORD=<your_mysql_password>
MYSQL_DATABASE=<your_mysql_database>

# Azure SQL Server
AZURE_SQL_SERVER=<your_azure_sql_server>
AZURE_SQL_DATABASE=<your_azure_sql_database>
AZURE_SQL_USER=<your_azure_sql_user>
AZURE_SQL_PASSWORD=<your_azure_sql_password>

# PostgreSQL Database
POSTGRES_HOST=<your_postgres_host>
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_DATABASE=<your_postgres_database>

# How to Run
Clone the repository and navigate to the project directory.
Set up the .env file with your database credentials.

Install the required libraries: pip install pymysql pyodbc psycopg2-binary python-dotenv

Run the python migration script.

# Usage
This tool is ideal for data engineering tasks requiring data migration or syncing across different database platforms, especially in cloud and multi-environment applications.

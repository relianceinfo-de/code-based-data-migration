import pymysql
import pyodbc
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# MySQL connection
mysql_conn = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

# Azure SQL Server connection using pyodbc
azure_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={os.getenv("AZURE_SQL_SERVER")};'
    f'DATABASE={os.getenv("AZURE_SQL_DATABASE")};'
    f'UID={os.getenv("AZURE_SQL_USER")};'
    f'PWD={os.getenv("AZURE_SQL_PASSWORD")}'
)

# Fetch data from MySQL
mysql_cursor = mysql_conn.cursor()
mysql_cursor.execute("SELECT * FROM tools")
data = mysql_cursor.fetchall()
columns = [desc[0] for desc in mysql_cursor.description]

# Create table in Azure SQL Server
azure_cursor = azure_conn.cursor()
drop_table_query = "DROP TABLE IF EXISTS tools_table"
azure_cursor.execute(drop_table_query)
azure_conn.commit()

create_table_query = """
CREATE TABLE tools_table (
    tool_name NVARCHAR(45),
    tool_type NVARCHAR(45),
    tool_use NVARCHAR(45),
    tool_category NVARCHAR(45)
)
"""
azure_cursor.execute(create_table_query)
azure_conn.commit()

# Insert data into Azure SQL Server
placeholders = ', '.join(['?'] * len(columns))
insert_query = f"INSERT INTO tools_table ({', '.join(columns)}) VALUES ({placeholders})"
azure_cursor.executemany(insert_query, data)
azure_conn.commit()

# Close all connections
mysql_cursor.close()
mysql_conn.close()
azure_cursor.close()
azure_conn.close()

print("Data migrated successfully to Azure SQL Server!")

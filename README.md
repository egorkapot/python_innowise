# Innowise_Python_Task1

**This project is for educational purposes only**

This project contains the following working files:
 - configs - folder that contains a working file
   -  conf_db.py - file with configuration settings
 - logg - folder that contains setup for logging
   -  logger_setup.py - file with setup
   -  debug.log - log file that saves log messages
   -  logging_conf.yml - configuration for logging
 -  modules - folder that contains classes that operate within database
    -  base_etl_class.py - abstraction class for ETL class
    -  etl.py  -  conduction of ETL process considering creation the schema with tables in database
    -  postgresdb.py - postgres class that contains ETL functions
 -  queries - folder that contains SQL queries
    -  query_age_diff.sql
    -  query_gender.sql
    -  query_list_of_rooms.sql
    -  query_lowest_avg_age.sql
    -  query_select_rooms.sql
    -  query_select_students.sql
    -  schema.sql  - query to create the schema and tables in database
 -  source - folder that contains files with the data
    -  input_data  - folder that contains input data
        - rooms.json - json with the information about rooms
        - students.json - json with the information about rooms
    -  output_data - folder is going to contain the final files
 -  tests - folder dedicated to conduct python tests
    -  queries_for_test  - contains simple SQL queries for testing
        - query_1.sql
        - query_2.sql
    -  config.json - config for creation the test connection
    -  conftest.py - testing file containing pytest fixtures
    -  test_config.py  - file that tests the configuration class
    -  test_postgres.db  - file that tests the postgres class
    -  test_queries.py - file that tests the queries class
 -  utils
    -  queries - class that creates dictionary of queries that extract the data from database
 -  .flake8 - configuration for flake8
 -  .gitignore
 -  .pre-commit-config.yml  - file with configuration for pre-commit
 -  main.py - main file that runs all processes
 -  precommit_requirements.txt  - requirements for pre-commit
 -  requirements.txt  - file that contains versions for modules




## Requirements

1. Python 3.10.6
2. PostgreSQL 15.1

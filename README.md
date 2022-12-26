# Innowise_Python_Task1

**This project is for educational purposes only**

## Description of the project
Having two jsons files there is a task to create a database and its schema with tables that should fit the data from jsons. Then these jsons need to be loaded into the database. Using the description of the required data, the data should be extracted from database and loaded as jsons. The workflow should be logged and tested using python tests.

## Description of the repository

This project contains the following working files:
 - configs - folder that contains a working file
   -  conf_db.py - file with configuration settings
   -  config.json - configuration for database in json file
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
    -  config_test.json - config for creation the test connection
    -  conftest.py - testing file containing pytest fixtures
    -  test_config.py  - file that tests the configuration class
    -  test_postgres.db  - file that tests the postgres class
    -  test_queries.py - file that tests the queries class
 -  utils
    -  queries - class that creates dictionary of queries that extract the data from database
 -  .flake8 - configuration for flake8
 -  .gitignore
 -  .pre-commit-config.yaml  - file with configuration for pre-commit
 -  main.py - main file that runs all processes
 -  precommit_requirements.txt  - requirements for pre-commit
 -  requirements.txt  - file that contains versions for modules
 - docker-compose.yml - compose file running database and custom python script images
 - Dockerfile - file that is creating a custom Docker image
 - run_script.bash - bash script to start the process    

## Requirements

1. Python 3.10.6
2. PostgreSQL 15.1
3. Docker - 20.10.22 
> not necessary if you run script using run_script.bash
4. Docker-compose 1.29.2 
> not necessary if you run script using run_script.bash

## Installation

Use ```pip install -r requirements.txt``` to install packages. If you are going to import your credentials by **.envrc** you need to download [direnv](https://direnv.net/docs/installation.html). Do not fortget to run ```direnv allow``` in your terminal

## Running the files using pre-commit

If you want to continue the development you can use **.pre-commit-config.yaml** to check and refactor your code. To do this just simply run ```pre-commit run --all-files --show-diff-on-failure``` in terminal

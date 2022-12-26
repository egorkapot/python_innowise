# Innowise_Python_Task1

**This project is for educational purposes only**

## Description of the project

The aim of this project is to show how you can connect to database, load files to database, implement some transformations and load the results on your local machine using Python. The code is written using Object-oriented programming concept. Workflow is logged and tested using python tests. There are two ways of how you can run this project and contribute here. We will discuss them below.

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
3. Docker 20.10.22 
4. Docker-compose 1.29.2 
> Installing these dependencies is not necessary if you run the script using run_script.bash

# Installation

There are two ways of working on this project. 
   -  Local development mode - working with the files in developer's mode
   -  Bash script mode - launching the files using bash script that builds Docker image and launches docker-compose build

Both require cloning the repository to your local machine

## Local Development Mode

In Local Development mode you need to have Python and PostgreSQL installed with versions mentioned above. Also you need to set up your own PostgreSQL database and put the configuration parameters into ```config.json``` file.

### Installing dependencies

Use ```pip install -r requirements.txt``` to install packages. If you are going to import your credentials by **.envrc** you need to download [direnv](https://direnv.net/docs/installation.html). Do not fortget to run ```direnv allow``` in your terminal

### Running the code

To run the code you need to lauch ```main.py``` file

### Performing python testing

All tests for this project are located in ```/tests/``` folder. You can create your own tests and run them by using the following command ```pytest --cov-report term-missing --cov=.```. To ignore files for testing you can amend ```.coveragerc``` file.

### Code refactoring using pre-commit

If you want to continue the development you can use **.pre-commit-config.yaml** to check and refactor your code. To do this just simply run ```pre-commit run --all-files --show-diff-on-failure``` in terminal

### Working with Dockerfile and docker-compose

 The repository contains Dockerfile and docker-compose for running the script. To run the script using docker-compose build you might need to have docker and docker-compose installed.

 #### Building the Docker image

 You can amend Docker file and add additional logic for building the image. Then you can build Docker image by running ```docker build -t #image_name``` in your terminal

 #### Running Docker-compose 

 After building your own image you need to edit **docker-compose** file and change ```image: #put_your_image_name``` in python service. Then run the ```docker-compose up -d``` command in your terminal 

## Docker installation mode

It is not necessary to have **docker** and **docker-compose** installed. You just need to run the ```sudo bash run_script.bash``` command in your terminal. This script will automatically install docker and docker-compose on your local machine *(this works only for Linux)*. After running the script docker will run the containers with Postgres database and modified Python script. You will receive the output files in ```source/output_data/``` folder on your local machine.

You might receive an error with docker-compose while running this script. It happens because multiple versions of docker-compose were installed. Open your terminal and write ```whereis docker-compose``` that shows all locations of docker-compose. Check if docker-compose is located in ```/local/usr/``` folder and if so remove this using ```sudo rm -r /local/usr/docker-compose```.


 

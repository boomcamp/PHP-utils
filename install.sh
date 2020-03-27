#! /usr/bin/env bash
set -x 

# Import and create environment variables 
echo USER='yourgithubusername' >.env  
echo PASSWORD='yourgihubpassword' >> .env 
echo REPO='boomcamp/PHP-ToyProblems-and-Activity-submissions' >> .env

# Configure virtual environment
pipenv install
pipenv shell

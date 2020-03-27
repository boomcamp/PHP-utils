#! /usr/bin/env bash
set -x 

# Import and create environment variables 
echo USER='yourgithubusername' >.env  
echo PASSWORD='yourgihubpassword' >> .env 
echo REPO='boomcamp/PHP-ToyProblems-and-Activity-submissions' >> .env

# Create containers for cloned submissions and screenshots
mkdir pulls/
mkdir captures/

# Add full priveledges
chmod 777 -R pulls/
chmod 777 -R captures/

# Configure virtual environment
pipenv install
pipenv shell

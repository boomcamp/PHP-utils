#! /usr/bin/env bash
set -x 

# Import and create environment variables 
echo USER='githubusername' >.env  
echo PASSWORD='githubpassword' >> .env 
echo REPO='boomcamp/PHP-ToyProblems-and-Activity-submissions' >> .env

# Create containers for cloned submissions and screenshots and add full priveledges
mkdir pulls/ && chmod 777 -R pulls/
mkdir captures/ && chmod 777 -R captures/

# Start localhost in new tab
gnome-terminal --tab --title="localhost:8000" -- /bin/sh -c 'echo starting localhost...; php -S localhost:8000'

# Configure virtual environment
pipenv install
pipenv shell

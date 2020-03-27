# About the utils

This Grading utility is built in `python3` and `asyncio` it clones the students `submission` branch it helps PHP instructor to create screenhsots and view the result and source code of students toy problems and activities.

To start clone this repository and create `captures/` and `pulls/` folder, you will need `python3`, `pip3` and `pipenv` installed in your machine. you can check [here](https://github.com/boomcamp/setup-pip-pipenv-django-admin-python3) the steps on how to configure a development environment.

### Proceedures on how to use the utils

1.) To start update `instal.sh` with your github `username` and `password` then activate virtual environment by typing:

```
$jino@mentor ~/utils $  ./install.sh
```

this will automatically create the `.env` file that will export in our python virtual environment.

2.) To store submissions to `submission/pulls/` folder type:

```
(utils) $jino@mentor ~/utils $ python3 pull.py
cloning.. HamletDelosReyes/PHP-ToyProblems-and-Activity-submissions submission
cloning.. jinolacson/PHP-ToyProblems-and-Activity-submissions submission
``` 

3.) Open up new terminal and start PHP cli by typing:

```
(utils) $jino@mentor ~/utils $  php -S localhost:8000 
PHP 7.2.24-0ubuntu0.18.04.3 Development Server started at Fri Mar 27 09:34:16 2020
Listening on http://localhost:8000
Document root is /home/jino/Downloads/utils
Press Ctrl-C to quit.
```

3.) Reactivate shell `pipenv shell` and start creating screenshots:

```
(utils) $jino@mentor ~/utils $  python3 capture.py
Creating screenshot..captures/jinolacson.png
```

4.) When done on checking type `pipenv --rm` to remove virtual enviroment.

```
$jino@mentor ~/utils $  pipenv --rm
Removing virtualenv (/home/jino/.local/share/virtualenvs/utils-7GKLs4q2)…
```

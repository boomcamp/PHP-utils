# About the utils

This Grading utility is built in `python3` and `asyncio` it clones the students `submission` branch it helps PHP instructor to create screenhsots and view the result and source code of students toy problems and activities.

You will need `python3`, `pip3` and `pipenv` installed in your machine. you can check [here](https://github.com/boomcamp/setup-pip-pipenv-django-admin-python3) the steps on how to configure a development environment.

### Proceedures on how to use the utils

1.) Open `install.sh` and update `USER` and `PASSWORD` with your github `username` and `password` then type.

```
$jino@mentor ~/PHP-utils $  ./install.sh
```

2.) Clone submissions into `pulls/` folder by executing this command:

```
(utils) $jino@mentor ~/PHP-utils $ python3 pull.py
cloning.. HamletDelosReyes/PHP-ToyProblems-and-Activity-submissions submission
cloning.. jinolacson/PHP-ToyProblems-and-Activity-submissions submission
``` 

3.) Start creating screenshots

```
(utils) $jino@mentor ~/PHP-utils $  python3 capture.py
Creating screenshot..captures/jinolacson.png
```

4.) When done on checking type `pipenv --rm` to remove virtual enviroment.

```
$jino@mentor ~/PHP-utils $  pipenv --rm
Removing virtualenv (/home/jino/.local/share/virtualenvs/utils-7GKLs4q2)…
```

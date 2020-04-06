# About the utils

This Grading utility is built in `python3` and `asyncio` it clones the students `submission` branches and create `screenshots` of toy problems and activities.

You will need `PHP7`, `python3`, `pip3` and `pipenv` installed in your machine. you can check [here](https://github.com/boomcamp/setup-pip-pipenv-django-admin-python3) the steps on how to configure a development environment.

### Procedures on how to use the utils

1.) Open `setup.sh` and update `USER` and `PASSWORD` with your github `username` and `password` then type.

```
$jino@mentor ~/PHP-utils $  ./setup.sh
```

2.) Clone and create the screenshots.

```
(PHP-utils) $jino@mentor ~/PHP-utils $ python3 capture.py
cloning.. HamletDelosReyes/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..HamletDelosReyes
Done.
cloning.. lancaster215/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..lancaster215
Done.
cloning.. rapraquion/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..rapraquion
Done.
cloning.. serra-vp/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..serra-vp
Done.
cloning.. ginoAquino7/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..ginoAquino7
Done.
cloning.. vanessadulva/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..vanessadulva
Done.
cloning.. jaymardmenor/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..jaymardmenor
Done.
cloning.. JeffreyMolleno/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..JeffreyMolleno
Done.
cloning.. markjowenamedes/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..markjowenamedes
Done.
cloning.. kojiadrianojr/PHP-ToyProblems-and-Activity-submissions submission
Creating screenshot..kojiadrianojr
Done.
``` 

3.) When done on checking type `pipenv --rm` to remove virtual enviroment.

```
$jino@mentor ~/PHP-utils $  pipenv --rm
Removing virtualenv (/home/jino/.local/share/virtualenvs/utils-7GKLs4q2)…
```

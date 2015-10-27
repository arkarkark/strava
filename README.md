Strava
======

suck data out of strava using [stravalib](https://github.com:hozn/stravalib/)

```shell
if ! which pip; then sudo easy_install pip; fi
sudo pip install units
sudo pip install stravalib
sudo pip install Django
sudo pip install tqdm
./manage.py migrate
./stravasuck.py

```

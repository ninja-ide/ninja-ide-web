ninja-ide-web v3.0
==================

##Website for NINJA-IDE
####This readme file is a work in progr

Just like Ninja-IDE version we are currently on development of the 3rd version of the site.


### TL;DR: I want to help you guys!!

Any help is welcome for creating new issues and taking care of free issues. You'll understand that we cannot let you add a dancing Jesus or a Mr X photo to our awesome ninja site for the simple reason that **we** are the ones that want to add that kind of staff to the site.

If you really really REALLY want to help us, just get to our site(http://ninja-ide.org) and donate what your heart says. From here we can hear it saying "more than 10 dollarssssss.... this guys deserve it.... I really enjoy watching soup-operas.... ". So, come on, be part of the awesome group of ninja suppliers.


### Get your own copy of the site (for development or learning):

    git clone git@github.com:ninja-ide/ninja-ide-web.git
    cd ninja-ide-web
    mkvirtualenv ninjaweb
    pwd >> $WORKON_HOME/ninjaweb/.project
    git checkout ninjaweb3
    pip install -r requirements/dev.txt

    cd mezza-ninja
    add2virtualenv .
    export DJANGO_SETTINGS_MODULE="settings.local"
    ./manage.py createdb
    ./manage.py runserver

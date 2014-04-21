ninja-ide-web v3.0
==================

##Website for NINJA-IDE
####This readme file is a work in progr

Just like Ninja-IDE version we are currently on development of the 3rd version of the site.


### TL;DR: I want to help you guys!!

Any help is welcome for creating new issues and taking care of free issues. You'll understand that we cannot let you add a dancing Jesus or a Mr X photo to our awesome ninja site for the simple reason that **we** are the ones that want to add that kind of staff to the site.

If you really really REALLY want to help us, just get to our site(http://ninja-ide.org) and donate what your heart says. From here we can hear it saying "more than 10 dollarssssss.... this guys deserve it.... I really enjoy watching soup-operas.... ". So, come on, be part of the awesome group of ninja suppliers.


### Get your own copy of the site (for development or learning):

    # clone the thing
    git clone git@github.com:ninja-ide/ninja-ide-web.git

    # create a virtualenv for it
    cd ninja-ide-web
    mkvirtualenv ninjaweb
    pwd >> $WORKON_HOME/ninjaweb/.project

    # install all requirements
    pip install -r requirements/dev.txt

    # prepare it
    cd mezzaninja
    add2virtualenv .
    export DJANGO_SETTINGS_MODULE="settings.local"
    ./manage.py syncdb --migrate
    ./manage.py runserver

#### Note
Currently there are a lot of files & code deprecated that belongs to previous version of site. After completing the refactoring those files won't exist anymore.

### You want to tune up the CSS?

Ninja-IDE is being developed using LESS precompiler. If you want to style and don't get crazy in the process then you better learn it once for all and be happy the rest of your life.

It's simple:

1) get the latest version of less

    npm install less

2) add the path where Less was installed to your PATH env.

    export PATH="$PATH:node_modules/less/bin"

3) Done. Was simple or what?

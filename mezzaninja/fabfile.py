from os import path
from fabric.api import env, run, cd, settings, abort
from django.conf import FAB_USER, FAB_SERVER

# Config
WEBFACTION_APP = 'ninjaweb3'
REPO_DIR_NAME = 'ninja-ide-web'
PROJECT_NAME = 'mezzaninja'
REPOSITORY = 'https://github.com/ninja-ide/ninja-ide-web.git'

# Enviroment config
env.hosts = [FAB_SERVER]
env.user = FAB_USER
env.webfaction_app_dir = path.join("~", "webapps", WEBFACTION_APP)
env.webfaction_repo_dir = path.join("~", "webapps", WEBFACTION_APP, REPO_DIR_NAME)
env.webfaction_apache_dir = path.join("~", "webapps", WEBFACTION_APP, "apache2")
env.webfaction_django_project = path.join("~", "webapps", WEBFACTION_APP, REPO_DIR_NAME, PROJECT_NAME)

# The following was commented becouse the webfaction docs have wrong params (ie: --target)
# https://docs.webfaction.com/software/python.html#installing-packages-with-pip
# PIP_INSTALL_EXECUTABLE = 'pip-2.7 install --target=$PWD/lib/python2.7 --install-option="--install-scripts=$PWD/bin"'
# PIP_UPDATE_EXECUTABLE = 'pip-2.7 install  --target=$PWD/lib/python2.7 --install-option="--install-scripts=$PWD/bin" --upgrade'
PIP_INSTALL_EXECUTABLE = 'pip-2.7 install --install-option="--install-scripts=$PWD/bin" --install-option="--install-lib=$PWD/lib/python2.7"'
PIP_UPDATE_EXECUTABLE = 'pip-2.7 install --install-option="--install-scripts=$PWD/bin" --install-option="--install-lib=$PWD/lib/python2.7" --upgrade'
PYTHON_EXECUTABLE = 'python2.7'


def backup_existing_repo():
    """
    Backup the current cloned/deployed repo if it exist
    """
    # with settings(warn_only=True):
    #     with cd(env.webfaction_app_dir):
    #         # TODO: if there a ninja-ide-web, backup it. Use a timestamp in name
    #     if output.failed:
    #         abort(output)
    print "backup_existing_repo: TO BE DONE"


def clone():
    """
    On production server, clone the ninjaweb repo
    """
    with settings(warn_only=True):
        with cd(env.webfaction_app_dir):
            output = run("git clone " + REPOSITORY)
        if output.failed:
            abort(output)


def commit():
    """
    On local machine, commit the new changes on branch master
    """
    print "commit: TO BE DONE"


def push():
    """
    On local machine, push the new commits to origin master
    """
    print "push: TO BE DONE"


def backup():
    """
    On production server, make a database backup
    """
    # with settings(warn_only=True):
    #     with cd(env.webfaction_app_dir):
    #         # TODO: if there a mezzaninja/settings/local.py,
    #         # backup it use a timestamp in name
    #     if output.failed:
    #         abort(output)
    print "backup: TO BE DONE"


def pull():
    """
    On production server, pull the new changes from origin master
    """
    with settings(warn_only=True):
        with cd(env.webfaction_repo_dir):
            output = run("git pull origin master")
        if output.failed:
            abort(output)


def install():
    """
    On production server, install all requirements
    """
    with settings(warn_only=True):
        with cd(env.webfaction_app_dir):
            output = run(PIP_INSTALL_EXECUTABLE + " -r " + REPO_DIR_NAME + "/requirements/prod.txt")
        if output.failed:
            abort(output)


def upgrade():
    """
    On production server, install all requirements
    """
    with settings(warn_only=True):
        with cd(env.webfaction_app_dir):
            output = run(PIP_UPDATE_EXECUTABLE + " -r " + REPO_DIR_NAME + "/requirements/prod.txt")
        if output.failed:
            abort(output)


def syncdb():
    """
    On production server, run the syncdb
    """
    with settings(warn_only=True):
        with cd(env.webfaction_django_project):
            output = run(PYTHON_EXECUTABLE + " manage.py syncdb")
        if output.failed:
            abort(output)


def migrate():
    """
    On production server, run the migrate
    """
    with settings(warn_only=True):
        with cd(env.webfaction_django_project):
            output = run(PYTHON_EXECUTABLE + " manage.py migrate")
        if output.failed:
            abort(output)


def collectstatic():
    """
    On production server, run the collectstatic
    """
    with settings(warn_only=True):
        with cd(env.webfaction_django_project):
            output = run(PYTHON_EXECUTABLE + " manage.py collectstatic --noinput")
        if output.failed:
            abort(output)


def restart():
    """
    On production server, restart the apache server
    """
    print("\n* Restarting server.")
    with settings(warn_only=True):
        with cd(env.webfaction_apache_dir):
            output = run("./bin/restart")
        if output.failed:
            abort(output)
    print("\n  Done.")


def test_connection():
    """
    Just a task for test the connection
    """
    print("\n* Testing connection.")
    with settings(warn_only=True):
        with cd(env.webfaction_repo_dir):
                output = run("ls")
        if output.failed:
            abort(output)
    print("\n  Done.")


def initialize():
    """
    If never have been deployed, run this.
    """
    backup_existing_repo()
    clone()


def prompt_backup():
    prompt = raw_input("\n>> Backup existing data? WARNING: NOT IMPLEMENTED YET!!\n(yes/no)\n>")
    if prompt.lower() == "yes":
        print("\n* Starting backup.")
        backup()
        print("\n  Done.")


def deploy():
    """
    Run all task to deploy the site.

    NOTE: you should run initialize() task before you can run this
    """

    #commit()
    #push()
    prompt_backup()

    pull()
    install()
    #upgrade()
    syncdb()
    #migrate()
    collectstatic()

    restart()

#!/bin/bash
#This bash script instantiates a django project and app
#Based on the user prompt imput.  At the current moment
#App will still need to be added to INSTALLED_APPS
#Within settings.py in project
read -p "Enter project name: " proj_name
read -p "Enter app name: " app_name
read -p "Enter virtual envrionment name: " venv_name
function makeapp {
    echo "$proj_name"
    echo "$app_name"
    django-admin startproject $proj_name
    cd $proj_name
    django-admin startapp $app_name
    mkvirtualenv $venv_name
    python manage.py runserver
}
makeapp
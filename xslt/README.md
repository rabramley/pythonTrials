# xslTransform

## Overview

Application to transform XML data

## Installation

Install required XML libraries

    sudo apt-get install libxml2-dev libxslt-dev python-dev

Then cd into the project directory and create a virtual environment for it.  Don't
worry, if you name it the same as me git will ignore it.

    virtualenv venv

Activate the virtual environment

    . venv/bin/activate

Then install lxml

    pip install lxml

The project contains a `data` folder that's contents are never checked in.
This is to protect the potentially sensitive data from accidentally being
uploaded to the internet.
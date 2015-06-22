#!/usr/bin/env python

import yaml

fileStream = open('data.yml', 'rb')

settings = yaml.load(fileStream)

print settings['a']
#!/usr/bin/env python

import yaml

textfile = 'data.yml'
fileStream = open(textfile, 'rb')

print yaml.dump(yaml.load(fileStream))
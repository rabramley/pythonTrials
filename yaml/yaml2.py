#!/usr/bin/env python

import yaml

fileStream = open('data.yml', 'rb')

print yaml.dump(yaml.load(fileStream))
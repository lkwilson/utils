#!/usr/bin/env python3

import pip
from subprocess import call

call('python3 -m pip install --upgrade pip', shell=True)
for dist in pip.get_installed_distributions():
    call('python3 -m pip install --upgrade '+dist.project_name, shell=True)

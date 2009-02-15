#!/usr/bin/env python

import json
import os
from jinja2 import Template


template = Template(file('projects.html').read())
projects = json.load(file('projects.json'))
print template.render(sections=projects)

#!/usr/bin/env python

import json
import os
from jinja2 import Template

__dir__ = os.path.realpath(os.path.dirname(__file__))
def f(n):
    return file(os.path.join(__dir__, n))

template = Template(f('projects.html').read())
projects = json.load(f('projects.json'))
print template.render(sections=projects)

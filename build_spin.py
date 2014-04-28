"""
Builds datebox into one file.  To build a new version, change the version
number and rerun.

M. Marino Apr 2014
"""

import urllib2 
import sys
import re

base_url = "http://fgnass.github.io/spin.js/"
version = "2.0.1"
module_name = "spin"
json_file = """{
    "name": "%(NAME)s",
    "version": "%(VERSION)s-kanso.1",
    "categories": ["visualization"],
    "maintainers": [
        {
            "name": "Michael Marino",
            "url": "https://github.com/mgmarino"
        }
    ],
    "url": "%(URL)s",
    "modules": "%(NAME)s.js",
    "modules_attachment": false,
    "dependencies": {
        "modules": ">=0.0.8"
    },
    "description": "Spin.js dynamically creates spinning activity indicators that can be used as resolution-independent replacement for AJAX loading GIFs.  This provides version %(VERSION)s."
}
""" % { 
        "NAME" : module_name, "VERSION" : version,
        "URL" : base_url 
      }

readme = """kanso-spin
==========

Kan.so export of spin.js

This is an export of spin.js for the kan.so system.  spin.js is developed by
Felix Gnass (https://github.com/fgnass/spin.js).

The current version provided here is %(VERSION)s. 
""" % { "VERSION" : version }
 
total_url = "%(BASE)s/spin.js" % { "BASE" : base_url }
core_data=""

try:
    dat = urllib2.urlopen(total_url)
    core_data += dat.read()
except urllib2.URLError, e:
    print e, t
    print "Exiting..."
    sys.exit(1)

open(module_name + ".js", "w").write(core_data)
open("kanso.json", "w").write(json_file)
open("README.md", "w").write(readme)

#!/usr/bin/python
###############################################################################
# Copyright (c) 2021
# Ivan Stanev
# All rights reserved.
###############################################################################

import json
import os
import re
import sys
import urllib2
import app_module_utils

ONE_DAY_IN_SECONDS = 60 * 60 * 24
ONE_MONTH_IN_SECONDS = 30 * 60 * 60 * 24
ONE_YEAR_IN_SECONDS = 365 * 60 * 60 * 24
BASE_PATH = '/etc/128technology/application-modules'
sys.path.append(BASE_PATH)

URL = 'https://bit.ly/t128apps'

MODULE_NAME = 'application-pack'
service_name = ''


def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, ONE_DAY_IN_SECONDS)

    response = urllib2.urlopen(URL)
    lines = response.readlines()

    for line in lines:
        matches = re.search("^(.*?),(.*?),([0-9./]+),(.*?),([0-9]*?),([0-9]*$)",
                            line)
        if matches is not None:
            service_name = matches.group(1)
            service_desc = matches.group(2)
            cidr = matches.group(3)
            proto = matches.group(4)
            port_from = matches.group(5)
            port_to = matches.group(6)

            port_range = [app_module_utils.AppIdBuilder.create_port_range
                          (port_from, port_to)]
            if (not proto or proto == ''):
                app_id.add_entry(service_name, cidr)
            else:
                app_id.add_entry(service_name, cidr, proto, port_range)
            app_id.error = ''
#        else:
#            app_id.error = 'No mappings found'

    app_id.write_to_disk()


if __name__ == '__main__':
    main()

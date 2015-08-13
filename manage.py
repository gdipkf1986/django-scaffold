#!/usr/bin/env python
import os
import sys

import platform
if __name__ == "__main__":

    if platform.system().lower() == "windows":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scaffold.spec.stage.settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scaffold.spec.prod.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

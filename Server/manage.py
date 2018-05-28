#!/usr/bin/env python
import os
import sys
from os.path import join, dirname
import dotenv

if __name__ == "__main__":
    envpath = join(dirname(os.path.realpath(__file__)), '../.env')
    dotenv.load_dotenv(dotenv_path=envpath)
    ##access env vars like this os.environ.get("RIOT_KEY"))
    ##print(os.getenv("RIOT_KEY")) 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Treeline.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

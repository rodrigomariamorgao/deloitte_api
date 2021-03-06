#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
from os import environ


def main():
    if "test" in sys.argv or "behave" in sys.argv:
        environ.setdefault("DJANGO_SETTINGS_MODULE", "deloitte_api.testing")
    else:
        environ.setdefault("DJANGO_SETTINGS_MODULE", "deloitte_api.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

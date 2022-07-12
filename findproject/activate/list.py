import sys

from findproject.activate.python_venv import activate_pipenv
from findproject.activate.shell import activate_clear
from findproject.config import load_config


def print_activate_scripts(project):
    activate = {"pipenv": activate_pipenv, "clear": activate_clear}
    config = load_config()["activate_builtin"]

    for key in config:
        script = activate[key](project)
        if script:
            print(script)


if __name__ == "__main__":
    print_activate_scripts(sys.argv[1])

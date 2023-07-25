import json
import os
import sys
from pathlib import Path


def load_config():
    xdg_config_home = os.environ.get(
        "XDG_CONFIG_HOME",
        os.path.join(os.environ.get("HOME", ""), ".config"),
    )
    try:
        with open(
            os.path.join(xdg_config_home, "findproject/config.json")
        ) as config_file:
            config = json.load(config_file)
            for project in config["project_dirs"]:
                project["path"] = Path(project["path"]).expanduser()

            if "additional_projects" in config:
                config["additional_projects"] = [
                    Path(project).expanduser()
                    for project in config["additional_projects"]
                ]

            return config
    except IOError as error:
        print(f"Couldn't load config: {error.strerror}")
        sys.exit(1)

import json
import sys
import os
from pathlib import Path


def load_config():
    xdg_config_home = os.environ.get(
        "XDG_CONFIG_HOME",
        os.path.join(
            os.environ.get("HOME", ""),
            ".config"
        ),
    )
    try:
        with open(os.path.join(xdg_config_home, "findproject/config.json")) as config_file:
            config = json.load(config_file)
            for project in config["project_dirs"]:
                project["path"] = Path(project["path"])
            return config
    except IOError as error:
        print(f"Couldn't load config: {error.strerror}")
        sys.exit(1)

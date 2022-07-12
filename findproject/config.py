import json
import os
from pathlib import Path


def load_config():
    xdg_config_home = os.environ.get(
        "",
        os.path.join(
            os.environ.get("HOME", ""),
            ".config"
        ),
    )
    with open(os.path.join(xdg_config_home, "findproject/config.json")) as config_file:
        config = json.load(config_file)
        for project in config["project_dirs"]:
            project["path"] = Path(project["path"])
        return config

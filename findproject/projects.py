from pathlib import Path
from typing import List

from config import load_config


def get_projects(project_dir: dict) -> List[Path]:
    projects = [
        path
        for path in project_dir["path"].expanduser().iterdir()
        if path.name
        not in project_dir["exclude"]
        + list(map(lambda x: x["path"], project_dir["subdirs"]))
        and path.is_dir()
    ]
    for subdir in project_dir["subdirs"]:
        subdir["path"] = project_dir["path"] / subdir["path"]
        projects.extend(get_projects(subdir))
    return projects


def print_projects():
    for project_dir in load_config()["project_dirs"]:
        for project in get_projects(project_dir):
            print(project.absolute())

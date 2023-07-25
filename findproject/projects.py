from pathlib import Path
from typing import List

from config import load_config


def get_projects(project_dir: dict) -> List[Path]:
    projects = [
        path
        for path in project_dir["path"].iterdir()
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
    config = load_config()
    for project_dir in config["project_dirs"]:
        for project in get_projects(project_dir):
            print(project.absolute())

    if "additional_projects" in config:
        for project in config["additional_projects"]:
            print(project.absolute())

from pathlib import Path
from typing import Optional


def activate_pipenv(project) -> Optional[str]:
    if (Path(project) / "Pipfile").exists():
        return str((Path(__file__).parent / "scripts/pipenv").resolve())
    return None

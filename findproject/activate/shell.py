from pathlib import Path


def activate_clear(_): 
    return str((Path(__file__).parent / "scripts/clear").resolve())

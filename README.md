# findproject

findproject allows you to quickly navigate to your projects. The directories containing your projects can be configured with a simple JSON file. Furthermore, you can add scripts to be executed after navigating to project directories.

## Installation

Install [fzf](https://github.com/junegunn/fzf) as a fuzzy finder.

Clone the repository, then create a single executable with zipapp and move it to `.local/bin`. Make sure `.local/bin` is in your path.

```
git clone https://github.com/m-gail/findproject
cd findproject
python3 -m zipapp findproject -p "/usr/bin/env python3"
mv findproject.pyz ~/.local/bin/findproject
```

You can then use findproject like this:

```
findproject list
findproject active /home/username/path/to/project
```

Or copy one of the scripts (`scripts/fp`, `scripts/fp_tmux`) to `.local/bin` and use it instead.

## Configuration

The configuration file is located at `~/.config/findproject/config.json` and looks like this:

```json
{
    "project_dirs": [
        {
            "path": "/path/to/your/projects",
            "exclude": [
                "project_to_exclude"
            ],
            "subdirs": [
                {
                    "path": "subdirectory_containing_more_projects",
                    "exclude": [
                        "tmp"
                    ],
                    "subdirs": []
                }
            ]
        }
    ],
    "activate_builtin": [
        "pipenv",
        "clear"
    ]
}
```

`project_dirs` contains all directories, which contain your projects, any directory in these will be shown in fzf, unless it is listed in `exclude` or `subdirs`.

`exclude` contains subdirectories that should not appear in fzf.

`subdirs` contains subdirectories, which are not projects themselves, but contain more projects.

`activate_builtin` specifies scripts that should be run after changing the directory.

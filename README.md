# findproject

findproject allows you to quickly navigate to your projects. The directories containing your projects can be configured with a simple JSON file. Furthermore, you can add scripts to be executed after navigating to project directories.

## Installation

Install ![fzf](https://github.com/junegunn/fzf) as a fuzzy finder.

Clone the repository, then install it with pip:

```
git clone https://gitlab.com/ihciM/findproject
pip3 install -e ./findproject
```

Make sure the `fp` script provided by the python package (typically located at `~/.local/bin/fp`) is in your path.

To be able to change the directory, the script has to be sourced, for easier usage, the following alias is recommended:

```
alias fp=". fp"
```

## Configuration

The configuration file is located at `~/.config/findproject/config.json` and looks like this:

```
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

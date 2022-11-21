import os
import click
from git import Repo

from fastapicli.default_py_content import main_py, start_py

@click.command()
@click.argument('project-name', nargs=1)
@click.option('--git-init', default=False)
def project(project_name: str, git_init: bool):
    click.echo(f'Generating project structure for \'{project_name}\'...')
    
    # create project dir
    os.mkdir(project_name)

    # create app and contents
    os.mkdir(f'{project_name}/app')
    # create core directory
    os.mkdir(f'{project_name}/app/core')
    # create routers directory
    os.mkdir(f'{project_name}/app/routers')
    # create service directory
    os.mkdir(f'{project_name}/app/services')
    # create models directory
    os.mkdir(f'{project_name}/app/models')

    # touch dependencies file
    os.close(os.open(f'{project_name}/app/core/dependencies.py', os.O_CREAT))

    # create default main.py
    with open(f'{project_name}/app/main.py', 'w') as fp:
        fp.write(main_py)

    with open(f'{project_name}/app/start.py', 'w') as fp:
        fp.write(start_py)

    # init git repo 
    if git_init:
        repo = Repo.init(project_name)
        assert not repo.bare

    # touch README file
    os.close(os.open(f'{project_name}/README.md', os.O_CREAT))
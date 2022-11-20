import os
import click
from git import Repo

@click.command()
@click.argument('project-name', nargs=1)
def project(project_name: str):
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
    main_py = """from fastapi import FastAPI\nfrom fastapi.responses import RedirectResponse\n\napp = FastAPI()\n\n@app.get('/')\nasync def root():\n\treturn RedirectResponse('/docs')\n"""
    with open(f'{project_name}/app/main.py', 'w') as fp:
        fp.write(main_py)

    start_py = """import uvicorn\n\n# Any necessary initialization for running the uvicorn server goes here\n\nif __name__ == '__main__':\n\tuvicorn.run('main:app', host='0.0.0.0', port=8080)\n"""
    with open(f'{project_name}/app/start.py', 'w') as fp:
        fp.write(start_py)

    # init git repo 
    repo = Repo.init(project_name)
    assert not repo.bare

    # touch README file
    os.close(os.open(f'{project_name}/README.md', os.O_CREAT))
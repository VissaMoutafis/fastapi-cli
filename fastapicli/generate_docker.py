import click
from fastapicli.default_py_content import dockerfile_content

@click.command(help='Generate Dockerfile for fastapi running')
def docker():
    click.echo('Generating Dockerfile...')
    with open('Dockerfile', 'w') as fp:
        fp.write(dockerfile_content)
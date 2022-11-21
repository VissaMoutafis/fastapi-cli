import click
from fastapicli.default_py_content import dockerfile_content

@click.command()
def docker():
    click.echo('Generating Dockerfile...')
    with open('Dockerfile', 'w') as fp:
        fp.write(dockerfile_content)
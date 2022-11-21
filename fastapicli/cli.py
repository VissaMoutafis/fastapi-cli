import click
from fastapicli.generate_project import project
from fastapicli.generate_docker import docker
from fastapicli.generate_utils import router, service, model

@click.group()
def cli():
    pass

@cli.group()
def generate():
    pass

generate.add_command(project)
generate.add_command(docker)
generate.add_command(router)
generate.add_command(service)
generate.add_command(model)
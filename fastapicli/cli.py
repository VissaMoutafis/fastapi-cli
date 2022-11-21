import click
from fastapicli.generate_project import project
from fastapicli.generate_docker import docker
from fastapicli.generate_utils import router, service, model

@click.group(help='CLI tool to automate boring development procedures.')
def cli():
    pass

@cli.group(help="Generate project structure and other boiler plate, keeping a structural standard.")
def generate():
    pass

generate.add_command(project)
generate.add_command(docker)
generate.add_command(router)
generate.add_command(service)
generate.add_command(model)
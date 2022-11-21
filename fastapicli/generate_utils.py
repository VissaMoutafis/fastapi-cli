import click
import os

from fastapicli.utils import parse_filename, create_path_hierarchy
from fastapicli.default_py_content import router_py, service_py, model_py


@click.command()
@click.argument('router-name', nargs=1)
def router(router_name):
    if router_name[-3:] == '.py': router_name = router_name[-3:]
    
    # get path prefixes, if any
    prefixes, filename = parse_filename(router_name)

    cur_path = os.getcwd() + '/app/routers/'
    create_path_hierarchy(prefixes, cur_path)
    
    click.echo(f'Generating router @ "app/routers/{"/".join(prefixes)}"...')

    # create the router file
    with open(f'{cur_path}/{router_name}.py', 'w') as fp:
        fp.write(router_py('/'.join([*prefixes,filename])))

@click.command()
@click.argument('service-name', nargs=1)
def service(service_name: str):
    if service_name[-3:] == '.py': service_name = service_name[-3:]
    
    # get path prefixes, if any
    prefixes, filename = parse_filename(service_name)

    cur_path = os.getcwd() + '/app/services'
    create_path_hierarchy(prefixes, cur_path)
    
    click.echo(f'Generating service @ "app/services/{"/".join(prefixes)}"...')

    # create the service file
    with open(f'{cur_path}/{service_name}.py', 'w') as fp:
        fp.write(service_py('_'.join([*prefixes,filename])))

@click.command()
@click.argument('model-name', nargs=1)
def model(model_name: str):
    if model_name[-3:] == '.py': model_name = model_name[-3:]

    # get path prefixes, if any
    prefixes, filename = parse_filename(model_name)

    cur_path = os.getcwd() + '/app/models'
    create_path_hierarchy(prefixes, cur_path)
    
    click.echo(f'Generating model @ "app/models/{"/".join(prefixes)}"...')

    # create the model file
    with open(f'{cur_path}/{model_name}.py', 'w') as fp:
        fp.write(model_py(filename))

if __name__ == '__main__':
    pass
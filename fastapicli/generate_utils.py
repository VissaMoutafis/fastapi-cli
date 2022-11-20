import click

@click.command()
@click.argument('router-name', nargs=1)
def router(router_name):
    click.echo('Generating router...')

@click.command()
@click.argument('service-name', nargs=1)
def service(service_name: str):
    click.echo('Generating service...')

@click.command()
@click.argument('model-name', nargs=1)
def model(model_name: str):
    click.echo('Generating model...')


if __name__ == '__main__':
    pass
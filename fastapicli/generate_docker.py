import os
import click

@click.command()
def docker():
    click.echo('Generating Dockerfile...')
    dockerfile_content = """FROM python

COPY ./requirements.txt requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
 
WORKDIR /app
COPY ./app /app

CMD ["python3", "start.py"]
"""
    with open('Dockerfile', 'w') as fp:
        fp.write(dockerfile_content)
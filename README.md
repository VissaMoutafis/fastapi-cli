# General
A lightweight FastAPI CLI for generating project structure, components and Dockerfile.

## Installation
In order to install this python package you need to install pip first
```bash
python3 -m pip install pip
```
Now you are ready to install the cli from the github repo, using the following command
```bash
pip3 install git+https://github.com/VissaMoutafis/fastapi-cli
```

## Usage
Currently the package provides routines to create 
- project folder hierarchies
- router files
- service files
- model files
- basic Dockerfile

Run `fastapi --help` to get a usage manual.

Some examples of commands are 
```bash
fastapicli generate project test-proj # generates a project under the directory name 'test-proj'
```

```bash
fastapicli generate router test-router # generates a new router file, named 'test-router.py'
```

```bash
fastapicli generate router dir1/dir2/test-router # generates a new router file, named 'test-router.py', in the path app/routers/dir1/dir2. Create dirs if not exist.
```

## License
MIT License

## Moving Forward
- [ ] Add more functionalities
- [ ] Support customized Dockerfiles
- [ ] Support docker-compose files generation
- [ ] Enhance router/service/model templates

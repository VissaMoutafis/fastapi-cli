main_py = """from fastapi import FastAPI\nfrom fastapi.responses import RedirectResponse\n\napp = FastAPI()\n\n@app.get('/')\nasync def root():\n\treturn RedirectResponse('/docs')\n"""

start_py = """import uvicorn\n\n# Any necessary initialization for running the uvicorn server goes here\n\nif __name__ == '__main__':\n\tuvicorn.run('main:app', host='0.0.0.0', port=8080)\n"""

dockerfile_content = """FROM python

COPY ./requirements.txt requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
 
WORKDIR /app
COPY ./app /app

CMD ["python3", "start.py"]
"""

def router_py(s): 
    return f"""from fastapi import APIRouter

router = APIRouter(prefix='/{s}')

@router.get('/default')
def router_test():
    return {{'/{s}/default': 'OK'}}
"""

def service_py(s): 
    return f"""from core.dependencies import *

def {s}_service_test():
    return {{'{s}_service': 'OK'}}
"""

def model_py(s: str): 
    return f"""from typing import List, Union
from pydantic import BaseModel

class {s.capitalize()}(BaseModel):
    name: str
    description: Union[str, None] = None
"""
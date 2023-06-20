import os
import time
from concurrent.futures.process import ProcessPoolExecutor
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi_utils.tasks import repeat_every
from starlette.background import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from webapp.ioc_container import Container
from webapp.widgets import widgets_router
from pydantic import BaseModel, Field

isTesting = os.getenv('TEST_MSV_ISUNITTESTING') == 'True'
app = FastAPI(title='test-mst', version='1.0.0')
n = 0

def setup_app(skip_network_init = False):
    try:
        container = Container()
        app.container = container
        origins = [
            'http://localhost',
            'https://localhost',
            'http://localhost:8000',
            'https://localhost:8000',
            'http://localhost:4200'
        ]
        app.add_middleware(
            CORSMiddleware,
            allow_origins = origins,
            allow_credentials = True,
            allow_methods = ['*'],
            allow_headers = ['*']
        )
        app.include_router(widgets_router)
    except Exception as e:
        print(str(e))

@app.on_event('startup')
@repeat_every(seconds=5)
def sync_method():
    global n
    n += 1
    message = f'Iteration message # {str(n)}'
    print(message)
    # while True:
    #     n += 1
    #     message = f'Iteration message # {str(n)}'
    #     print(message)
        # time.sleep(5)

if not isTesting:
    setup_app()

from fastapi import FastAPI
from loguru import logger
from environs import Env
from container import Container


def on_startup():
    pass


def on_shutdown():
    pass


app = FastAPI(
    title="WDberries",
    on_startup=on_startup(),
    on_shutdown=on_shutdown()
)

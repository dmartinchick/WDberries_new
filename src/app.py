from fastapi import FastAPI


def on_startup():
    pass


def on_shutdown():
    pass


app = FastAPI(
    title="WDberries",
    on_startup=on_startup(),
    on_shutdown=on_shutdown()
)

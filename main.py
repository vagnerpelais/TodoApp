from fastapi import FastAPI
from database import engine
from routers import auth, todos
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse
import models


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def root():
    return RedirectResponse(url='/todos', status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)


models.Base.metadata.create_all(bind=engine)

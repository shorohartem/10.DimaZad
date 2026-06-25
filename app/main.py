
from fastapi import FastAPI, APIRouter
import uvicorn

from app.api.health import router as health_router
from app.api.crypto import router as crypto_router

routers: tuple[APIRouter, ...] = (
    health_router,
    crypto_router,
)

app = FastAPI()

for router in routers:
    app.include_router(router)



if __name__ == '__main__':
    uvicorn.run(app,
                host='0.0.0.0',
                port=8000,
                )

import uvicorn
from fastapi import APIRouter
from fastapi import FastAPI

from endpoints.config import config_router
from endpoints.feature_data import feature_data_router
from endpoints.model_file import models_router
from endpoints.schema import schema_router

app = FastAPI(title='Configuration')

router = APIRouter()
router.include_router(config_router, prefix='/tenants')
router.include_router(schema_router, prefix='/schema')
router.include_router(feature_data_router, prefix='/feature_data')
router.include_router(models_router, prefix='/model-files')

app.include_router(router)


@app.on_event('startup')
async def on_app_start():
    """Anything that needs to be done while app starts
    """
    pass


@app.on_event('shutdown')
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown
    """
    pass


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5005)

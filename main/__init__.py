from fastapi import FastAPI
from .logger import logger
from .data.utilities import DataManager


tags_metadata = [
    {
        "name": "general",
        "description": "General system level APIs",
    },
]


def create_app() -> FastAPI:
    logger.info(f'Initialising App Factory')
    app = FastAPI(
        debug=True, title="Surfers FastAPI Accelerator",
        description="REST APIs for surf system",
        version="0.1.0",
        openapi_url="/api/v1/api-docs",
        openapi_tags=tags_metadata
    ) 

    logger.info(f'Setup database')
    DataManager.initDB()

    logger.info(f'Create routers')

    from .apis.general import router as general_router
    app.include_router(general_router)

    return app

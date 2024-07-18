from fastapi import FastAPI
from app.routes import *


def create_app() -> FastAPI:
    # instantiate routes
    user_router = create_user_router()

    # instantiate app
    app = FastAPI(
        title="Prioritization Strategy Tool",
        description="Backend services",
    )

    # include routes in app
    app.include_router(user_router)

    return app


app = create_app()

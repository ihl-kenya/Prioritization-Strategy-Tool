from fastapi import FastAPI
from app.routes import *


def create_app() -> FastAPI:
    # instantiate routes
    user_router = create_user_router()
    facility_router = create_facility_router()

    # instantiate app
    app = FastAPI(
        title="Prioritization Strategy Tool",
        description="Backend services"
    )

    # include routes in app
    app.include_router(user_router)
    app.include_router(facility_router)

    return app


app = create_app()

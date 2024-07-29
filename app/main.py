from fastapi import FastAPI
from app.routes import *


def create_app() -> FastAPI:
    # instantiate routes
    user_router = create_user_router()
    facility_router = create_facility_router()

    # instantiate app
    server = FastAPI(
        title="Prioritization Strategy Tool",
        description="Backend services"
    )

    # include routes in app
    server.include_router(user_router)
    server.include_router(facility_router)

    return server


app = create_app()

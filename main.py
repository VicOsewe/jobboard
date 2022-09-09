from fastapi import FastAPI
from pkg.application.core.config import settings
from fastapi.staticfiles import StaticFiles
from pkg.infrastructure.db.session import engine   
from pkg.infrastructure.db.base import Base  
from pkg.presentation.apis.base import api_router


def include_router(app):
	app.include_router(api_router)


def create_tables():
    print("Creating tables...")          
    Base.metadata.create_all(bind=engine)

def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	create_tables()       
	return app


app = start_application()


from aiohttp import web
from app.forum.routes import setup_routes as setup_forum_routes
import aiohttp_jinja2
import jinja2


def setup_routes(application):
    setup_forum_routes(application)


def setup_external_libraries(application: web.Application) -> None:
    aiohttp_jinja2.setup(application,
         loader=jinja2.FileSystemLoader("templates")
    )


def setup_app(application):
    setup_external_libraries(application)
    setup_routes(application)
    print('app setup succeed')


app = web.Application()

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app)

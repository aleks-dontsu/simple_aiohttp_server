from aiohttp import web
from app.forum import views


def setup_routes(app):
    app.router.add_get("/", views.index)

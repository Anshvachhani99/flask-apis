import re
import time
import json
import logging
from aiohttp import web
from aiohttp.http_exceptions import BadStatusLine


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    try:
        file_path = "./templates/index.html"
        with open(file_path, "rb") as f:
            content = f.read()
        return web.Response(body=content, content_type="text/html")
    except FileNotFoundError:
        raise web.HTTPNotFound()
    except Exception as e:
        logging.error(f"Error serving index.html: {e}")
        raise web.HTTPInternalServerError()

print("done")

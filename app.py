from aiohttp import web


routes = web.RouteTableDef()

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

app = web.AppRunner(await web_server())



async def handle(request):
    return web.Response(text="Hello, World!")

app.router.add_get('/', handle)

await app.setup()
bind_address = "0.0.0.0" 
await web.TCPSite(app, bind_address,5001).start()

if __name__ == '__main__':
    web.run_app(app)

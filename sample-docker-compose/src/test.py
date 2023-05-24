import aiohttp
from aiohttp import web
import urllib.parse
import redis

class A():

    async def hc(self,request):
        status_code = 200
        url_params=request.query
        print(url_params)
        query = {}
        for key, val in url_params.items():
            query[key] = urllib.parse.quote(val)#.encode('utf-8')
        print(query)
        print(type(query))
        for i in query:
            print(type(query[i]))
        r = redis.Redis(host='my-redis-server', port=6379, password='')
        visitord = r.get("visitors")
        if visitord:
            pass
        else:
            r.set("visitors",1)

        print("visitors",visitord)
        visitord=int(visitord)+1
        r.set("visitors", visitord)
        response = 'Success, Status Code:' + str(visitord)
        return web.Response(text=response, status=status_code)

    async def hc1(self,request):
        s="sdsds"
        response = ('Success, Status Code:')
        return web.Response(text=response)


if __name__=='__main__':
    app=web.Application()
    handle=A()
    app.router.add_get('/hc',handle.hc)
    app.router.add_get('/', handle.hc1)
    web.run_app(app,port='5555')

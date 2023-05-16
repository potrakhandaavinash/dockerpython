#!/usr/bin/python3
import redis
from aiohttp import web




class A():
        async def hc(self,request):
            r = redis.Redis(host='add the ip address', port=6379, password='')
            visitord = r.get("visitors")
            if visitord:
                pass
            else:
                r.set("visitors",1) 

            print("visitors",visitord)
            visitord=int(visitord)+1
            r.set("visitors", visitord)
            response = 'Success, Status Code:' + str(visitord)
            return web.Response(text=response)

if __name__=='__main__':
    app=web.Application()
    handle=A()
    app.router.add_get('/hc',handle.hc)
    web.run_app(app,port='5555')

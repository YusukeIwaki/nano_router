# -*- coding:utf-8 -*-

from router import Router
from sub_router import router as subRouter

router = Router()

@router.Route("GET /")
def index(obj):
    print "index:", obj
    return subRouter.handle(obj["type"], obj)

@router.Route("GET /ping")
def ping(obj):
    print "ping", obj
    return "pong"

@router.DefaultRoute
def no_route(obj):
    print "no_route", obj
    return "404"

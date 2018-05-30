# -*- coding:utf-8 -*-

from router import Router

router = Router()

@router.Route("x")
def handle_type_x(obj):
    print "handle_type_x", obj
    return "OK"

@router.DefaultRoute
def handle_unknown_type(obj):
    print "handle_unknown_type:", obj
    return "NG"


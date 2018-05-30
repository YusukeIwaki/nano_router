# -*- coding:utf-8 -*-

from regex_router import RegexRouter

router = RegexRouter()

@router.Route("GET /.*")
def get(obj):
    return "GET", obj

@router.Route("POST /.*")
def post(obj):
    return "POST", obj

@router.DefaultRoute
def unknown(obj):
    return "unknown", obj

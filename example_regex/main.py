# -*- coding:utf-8 -*-

from main_router import router as app

def handle(obj):
    return app.handle("%s %s"%(obj["method"], obj["path"]), obj)

print handle({
    "method": "GET",
    "path": "/"
})

print handle({
    "method": "POST",
    "path": "/users",
    "header": {
        "Content-Type": "application/json"
    },
    "body": {
        "user": {
            "name": "YusukeIwaki"
        }
    }
})

print handle({
    "method": "DELETE",
    "path": "/users/1"
})
# -*- coding:utf-8 -*-

from main_router import router as app

print app.handle("GET /", {"type": "x", "data": "x"})
print app.handle("GET /", {"type": "y", "notification":"y"})
print app.handle("GET /ping", {"b": "b"})
print app.handle("GET /favicon.ico", {"hoge", "hoge"})

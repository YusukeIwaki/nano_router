# -*- coding:utf-8 -*-

import functools

class Router:
    def __init__(self):
        self._routes = {}
        self._default_route = None
        self.DefaultRoute = self._defaultRoute()
    
    def Route(self, routeId):
        def decorator(f):
            @functools.wraps(f)
            def wrapfunc(*args, **kwargs):
                return f(*args, **kwargs)
            self._routes[routeId] = wrapfunc
            return wrapfunc
        return decorator
    
    def _defaultRoute(self):
        def decorator(f):
            @functools.wraps(f)
            def wrapfunc(*args, **kwargs):
                return f(*args, **kwargs)
            self._default_route = wrapfunc
            return wrapfunc
        return decorator

    def handle(self, routeId, *args, **kwargs):
        if routeId in self._routes:
            return self._routes[routeId](*args, **kwargs)
        else:
            if callable(self._default_route):
                return self._default_route(*args, **kwargs)
            else:
                return None

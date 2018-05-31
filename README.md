# Nano Router: A very tiny router library.

## Say "Good-bye!" to boring if-clauses!

```py
def handle_request(obj):
  if obj["method"] == "GET":
    return handle_get(obj)
  elif obj["method"] == "POST":
    return handle_post(obj)
  else:
    return handle_unknown(obj)

def handle_get(obj):
  if obj["path"] == "/":
    return "OK"
  elif obj["path"] == "/ping":
    return "pong"
  else:
    return "404"

 :
 :
 :
 :

```

## Do it smart and simple way!

### main_router.py

```py
from nano_router import RegexRouter
from sub_router import router as sub

router = RegexRouter()

@router.Route("^GET /.*")
def handle_get(obj):
  return sub.handle(obj["path"], obj)

@router.Route("POST /.*")
def handle_post(obj):
  return "OK"

@router.DefaultRoute
def handle_known_request(obj):
  return "500"
```

### sub_router.py

```py
from nano_router import RegexRouter

router = RegexRouter()

@router.Route("/")
def get_index(obj):
  return "index"

@router.Route("/ping")
def get_ping(obj):
  return "pong"

@router.DefaultRoute
def get_default(obj):
  return "404"
```

### main.py

```py
from main_router import router

def handle(obj):
  print router.handle("%s %s"%(obj["method"], obj["path"]), obj)

handle({ "method": "GET", "path": "/" })
# => index

handle({ "method": "GET", "path": "/ping" })
# => pong

handle({ "method": "GET", "path": "/favicon.ico" })
# => 404

handle({
  "method": "POST", "path": "/users",
  "body": {
    "user": { "name": "YusukeIwaki" }
  }
})
# => OK

handle({ "method": "DELETE", "path": "/users/1" })
# => 500
```

## Install

### via 'pip install'

```
pip install git+https://github.com/YusukeIwaki/nano_router
```

### or "Copy & Paste" simply 😁

* https://github.com/YusukeIwaki/nano_router/blob/master/nano_router/router.py
* https://github.com/YusukeIwaki/nano_router/blob/master/nano_router/regex_router.py
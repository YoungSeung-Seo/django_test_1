from .common import *

INSTALLED_APPS += [
    "debug_toolbar",
]

# 이렇게 해주면 리스트 첫 부분에 추가가 된다.
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware",] + MIDDLEWARE


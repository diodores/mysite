from django.urls import path, re_path
from women.views import *

urlpatterns = [
    path('', index),
    path('cats/<int:catid>/', categories),
    re_path(r'^archive/(?<year>[0-9]{4}/)', arhive)
]

handler404 = pageNotFound

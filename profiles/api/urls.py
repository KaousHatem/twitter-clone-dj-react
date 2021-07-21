from django.urls import path

from .views import (
    user_follow_view,
)
'''
CLIENT
Base ENDPOINT /api/tweets/
'''
urlpatterns = [
    path('<str:username>/follow', user_follow_view),
]
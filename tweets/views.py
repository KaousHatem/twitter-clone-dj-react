
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.conf import settings


# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request, *args, **kwargs):
    # print(request.user)
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "pages/home.html",context={'username':username},status=200)

def tweets_list_view(request, *args, **kwargs):
    # print(request.user)
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "tweets/list.html")

def tweets_detail_view(request, tweet_id, *args, **kwargs):
    # print(request.user)
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "tweets/detail.html",context={'tweet_id':tweet_id})


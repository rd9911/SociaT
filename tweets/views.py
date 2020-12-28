import random
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings

from tweets.models import Tweet
from .forms import TweetForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.

def home_page(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)
    
def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        # DO OTHER VALIDATION LOGICS
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201) # 201 = for created items
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={'form': form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        'isUser': False,
        'response': tweets_list
    }
    return JsonResponse(data)


def tweet_details(request, tweet_id, *args, **kwargs):
    """def home_page(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)
    
    REST API VIEW
    Consume by js
    return json data
    """
    data = {
        "id": tweet_id,
        # "content": obj.content,
        # 'image_path': obj.image.url, 
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    ### Improve exception part so that only not valid ids will be 404
    except:
        data['message'] = 'Not Found'
        status = 404
    
    return JsonResponse(data, status=status)
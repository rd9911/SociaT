from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from tweets.models import Tweet
# Create your views here.


def home_page(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)
    
def tweet_details(request, tweet_id, *args, **kwargs):
    """
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
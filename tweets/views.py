from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse   
from .models import Tweet
# Create your views here.
def home_views(request,*args,**kwargs):
    #return HttpResponse("<h1>HELLO WORLD</h1>")
    return render(request,"pages/home.html",context={},status=200)

def home_views_id_html(request,tweet_id,*args,**kwargs):

    try:
        obj = Tweet.objects.get(id=tweet_id)
    except: 
        raise Http404
    return HttpResponse(f"<h1>HELLO WORLD {obj.content}</h1>")
def home_views_id_json(request,tweet_id,*args,**kwargs):
    """
    REST API VIEW
    RETURN json data
    """
    data ={

    }
    status= 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['id'] = obj.id
        data['content'] = obj.content
    except: 
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data,status=status)

def tweet_list_view(request,*args,**kwargs):
    """
    REST API VIEW
    RETURN json data
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id,"content":x.content} for x in qs]
    data = {
        "response":tweets_list
    }
    return JsonResponse(data)
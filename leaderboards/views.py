from django.http import HttpResponse 
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from leaderboards.models import Score

# Create your views here.
def index(request):
    top = Score.objects.order_by('points')
    top = top.reverse()[:10]
    output = json.dumps([{"name": q.username, "score": q.points} for q in top]) 
    return HttpResponse(output)

@csrf_exempt
def add_score(request):
    if request.method == "POST":
        body = json.loads(request.body)
        print(body)
        name = body["username"]
        if(Score.objects.filter(username=name).count() == 0):
            newScore = Score(username=body["username"], points=int(body["score"]))
            newScore.save()
            return HttpResponse("User Added Successfully")
        else:
            Score.objects.filter(username=name).update(points=int(body['score']))
            return HttpResponse("User Point Updated")
    return HttpResponse("Get Request")
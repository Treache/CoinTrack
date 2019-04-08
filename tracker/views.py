from django.shortcuts import render
from django.http import HttpResponse
from tracker import apiaccess
# Create your views here.

def index(request):
    # return HttpResponse("Hello From Server")
    jj = apiaccess.get_data()
    return render(request, 'tracker/index.html', {
        'title' : 'DASH, ETC, and LTC in USD',
        'data' : jj
    })
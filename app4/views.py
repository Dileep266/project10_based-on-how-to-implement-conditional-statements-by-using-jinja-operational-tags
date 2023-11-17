from django.shortcuts import render

# Create your views here.
def nested(request):
    d={'a':10,'b':90,'c':800}
    return render(request,'nested.html',d)

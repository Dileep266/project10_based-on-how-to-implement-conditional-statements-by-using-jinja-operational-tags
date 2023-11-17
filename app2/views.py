from django.shortcuts import render

# Create your views here.
def ifelsecondition(request):
    d={'a':130,'b':120}
    return render(request,'ifelsecondition.html',d)
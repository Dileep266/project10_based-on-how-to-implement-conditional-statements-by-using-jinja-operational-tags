from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    d={'a':101}
    return render(request,'ifcondition.html',d)
from django.shortcuts import render

# Create your views here.
def ifelseelifcondition(request):
    d={'a':10,'b':9,'c':20}
    return render(request,'ifelseelifcondition.html',d)

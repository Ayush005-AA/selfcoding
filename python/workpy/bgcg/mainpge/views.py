from django.shortcuts import render,HttpResponse

# Create your views here.
def homefun(request):
    return render(request,"home.html")
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'yourname': request.POST['yourname']
    }
    return render(request,'index.html',context)

def results(request):
    pass

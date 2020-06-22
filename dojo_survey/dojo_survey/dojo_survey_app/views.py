from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def results(request):
    if request.method =='POST':
        context = {
            'yourname': request.POST['yourname'],
            'lang': request.POST['location'],
            'loc': request.POST['language']
        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'lang': request.POST['location'],
            'loc': request.POST['language']
        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')

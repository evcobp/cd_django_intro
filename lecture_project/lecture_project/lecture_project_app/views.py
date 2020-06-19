from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # first time user experience
    if 'username' not in request.session:
        request.session['username'] = 'New User'
        
    context = {
        'username': request.session['username']
    }
    return render(request, 'index.html')

def create(request):
    print(request.POST['username'])
    request.session['username'] = request.POST['username']
    return redirect ('/')
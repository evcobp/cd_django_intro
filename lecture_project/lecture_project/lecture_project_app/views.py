from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # first time user experience
    if 'username' not in request.session:
        request.session['username'] = 'New User'

    context = {
        'username': request.session['username']
    }
    return render(request, 'index.html', context)

def create(request):
    print(request.POST['username'])
    request.session['username'] = request.POST['username']
    return redirect ('/')

def game(request):
    if 'username' not in request.session:
        request.session['username'] = 'New User'
    # check to see if I have started game
    if 'count' not in request.session:
        request.session['count'] = 0
    
    context = {
        'username': request.session['username'],
        'times': request.session['count']
    }
    return render(request, 'game.html', context)

def click(request):
    # Handle click
    request.session['count'] += 1
    return redirect('/game')

def reset(request):
    # Handle reset

    #remove everything from session
    # request.session.clear()

    #remove one thing from session
    del request.session['count']
    return redirect('/game')  
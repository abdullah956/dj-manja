from django.shortcuts import render

def home_view(request):
    # Data to pass to the template
    context = {'message': 'Welcome to my Django App!'}
    return render(request, 'home.html', context)

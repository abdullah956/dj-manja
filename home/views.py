from django.shortcuts import render

def asset_tracking(request):
    return render(request, 'home/asset_tracking.html')

def dashboard_main(request):
    return render(request, 'home/dashboard_main.html')

def groups(request):
    return render(request, 'home/groups.html')

def integrations(request):
    return render(request, 'home/integrations.html')

def members(request):
    return render(request, 'home/members.html')

def reports(request):
    return render(request, 'home/reports.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def registration(request):
    return render(request, 'registration.html')

def resetpassword(request):
    return render(request, 'resetpassword.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

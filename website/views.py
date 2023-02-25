from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session.set_expiry(86400)
            auth.login(request, user)
            return render(request, 'website/index.html')
        else:
            return render(request, 'website/login_failed.html', {'form': auth.forms.AuthenticationForm})
    else:
        return render(request, 'website/login.html', {'form': auth.forms.AuthenticationForm})


@login_required
def index(request):
    return render(request, 'website/index.html')








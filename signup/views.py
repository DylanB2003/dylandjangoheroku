from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

def index(request):
    return render(request,'signup/index.html')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'signup/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)


# @login_required
def api(request):
    if request.method == "POST":

        email1 = request.POST.get('email1')

        url = 'https://leakcheck.net/api/public?key=ca8ef477a088b5a822f05c61aa6c0fb7ef82e13b&check={}&type=email'.format(email1)

        response = requests.request("GET", url, verify=False)

        details = response.json()

        if details['success']:

            news = details['sources']

        else:

            news = ""

        return render(request, 'info.html', {'news': news})
    else:
        return render(request, 'info.html')
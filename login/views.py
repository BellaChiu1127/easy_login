from django.shortcuts import render
from .models import SignUp
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
def vendor_index(request):

    user_list = SignUp.objects.all()
    context = {'user_list':user_list}
    return render(request,'logins/login_detail.html',context)
def vendor_create_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SignUpForm()

    context = {
        'form' : form
    }
    return render(request, "logins/login_create.html", context)
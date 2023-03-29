from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from account.forms import UserRegisterForm
# Create your views here.


def register_account(request):

    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("accountLogin")

   # form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "account/login.html", context=context)
def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            user = authenticate(username=informacion['username'], password=informacion['password'])

            if user:
                login(request, user)

                return redirect("AppKalizAlfajores")
            else:
                return redirect("AppKalizInicio")

    form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, "account/login.html", context=context)
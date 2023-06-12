from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views import View


class SignUp(View):

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        template_name = 'users/signup.html'
        return render(request, template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)
            print(user)
            return redirect('home')
        return HttpResponse('Something went wrong in registration')

class SignIn(View):

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        template_name = 'users/signin.html'
        return render(request, template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Inactive user.")
        else:
            return redirect('sign-in')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')

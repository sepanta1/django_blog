from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserResgisterForm


def register(request):

    if request.method == 'POST':
        form = UserResgisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {user_name}!')
            # using the name we gave to url
            return redirect('blog-home')
    else:
        form = UserResgisterForm()
        # Create your views here.
    return render(request, 'users/register.html', context={'form': form})

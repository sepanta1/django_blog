from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserResgisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register(request):

    if request.method == 'POST':
        form = UserResgisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {user_name}!')
            # using the name we gave to url
            return redirect('login')
    else:
        form = UserResgisterForm()
        # Create your views here.
    return render(request, 'users/register.html', context={'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            messages.success(request, f'Your account has been updated!')
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form, }
    return render(request, 'users/profile.html', context=context)

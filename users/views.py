from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import \
    LoginRequiredMixin
from django.contrib.auth.mixins import \
    UserPassesTestMixin 

from .forms import UserRegisterForm, UserUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Welcome {first_name}! Your account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.instance.first_name = user_form.instance.first_name.title()
            user_form.instance.last_name = user_form.instance.last_name.title()
            user_form.save()
            messages.success(request, f'Done! Info succesfully updated')

            return redirect('profile') 
    else:
        user_form = UserUpdateForm(instance=request.user)
    

    context = {
        'user_form': user_form
    }

    return render(request, 'users/profile.html', context)

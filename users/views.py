from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import \
    LoginRequiredMixin  # inherit this class in order to require authentication for class based views
from django.contrib.auth.mixins import \
    UserPassesTestMixin  # inherit this class in order to check if the user should access the view even if authenticated

from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.
def register(request):

    # Conditional logic to check if the current HTTP method is actually a POST method
    # So we can create an instance of the form with the data which is passing in by the POST method
    # In order to validate that data, because a POST data could carry pretty much anything, and we don't want that
    # Otherwise, a blank instance of the form is created, since it's probably a GET method (when we navigate to the register page for example)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # If the form has valid data when submited...
            form.save()
            first_name = form.cleaned_data.get('first_name') # The validated data will be accessible by the "cleaned_data" method
            messages.success(request, f'Welcome {first_name}! Your account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm() # It makes use of a Django's pre backed form called UserCreationForm which is instantiated inside forms.py file
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # request.POST means we want the data which the user filled out into the form to update the current instance data
        # instance=request.object means you want to populate the empty form instance with the current user data
        # E.g.: UserUpdateForm() would create an empty form (Not good for UX at all)
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.instance.first_name = u_form.instance.first_name.title() # title is a python string method to capitalize the initials for each word of a string
            u_form.instance.last_name = u_form.instance.last_name.title()
            u_form.save()
            messages.success(request, f'Done! Info succesfully updated')

            # We are using the redirect method here in order to avoid POST-GET Redirect Pattern
            # Which will cause the browser to ask if you want to re-submit the form information since it's about to
            # Use a POST method in the 'render' method, so we use 'redirect' method instead which you make use of a GET method
            # P.S. render method is still need by the end of the view function, because it's responsible to manage the 
            # Request and the context to the template
            return redirect('profile') 
    else:
        # If it's a GET request, that means the user just navigated to the Profile Info screen
        # So a filled form is the only thing we want, once we have no information passing through a POST method
        u_form = UserUpdateForm(instance=request.user)
    

    context = {
        'u_form': u_form
    }

    return render(request, 'users/profile.html', context)

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm # to get a user registration page we can remove this after getting the new inherited form from .forms
from django.contrib import messages
from . forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required # this is to make sure certain functionalities are accessible only when user is logged in

def register(request):
    # create and instance of the user creation form class
    #form = UserCreationForm() # this is the context 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # we want to create a form where we have the data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}!,You will now be able to login')
            # return redirect('blog-home') this was routing to blog home page
            return redirect('login')
    else:    
        form = UserRegisterForm() 
    return render(request,'users/register.html',{'form': form}) # 3rd argument is a dict 

@login_required
def profile(request):
    if request.method == 'POST': # this is to check if the method is post only then we will create instances
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Profile updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request,'users/profile.html',context)
    
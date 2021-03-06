from django.shortcuts import render, redirect
from django.urls import reverse

from vips.models import GlUser
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'base.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            address = form.cleaned_data['address']
            sex = form.cleaned_data['sex']
            birthday = form.cleaned_data['birthday']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            gluser = GlUser(GL_customer=user, GL_username=user.username,
                            GL_address=address, GL_birthday=birthday,
                            GL_customer_id=user.id, GL_email=email,
                            GL_sex=sex, contact=contact)
            gluser.save()
            return redirect('/accounts/login')
        else:
            print('123412341234')
            return redirect(reverse('accounts:register'))
    if request.method == "GET":
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)




@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        print(form)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')

#
# def my_view(request):
#     print(request.POST)
#     username = request.POST['Username']
#     password = request.POST['Password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('home:index')
#
#     else:
#         return "Haven't register yet?"

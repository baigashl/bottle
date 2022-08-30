from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import Post


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Wellcome {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_posts = Post.objects.filter(author=request.user)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_posts': user_posts
    }
    return render(request, 'users/profile.html', context)


@login_required
def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    posts = Post.objects.filter(author_id=pk)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'users/user_detail.html', context)


class DeleteUser(SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_message = "User has been deleted"
    success_url = reverse_lazy('blog-home')


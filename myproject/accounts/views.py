from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from .forms import SignUpForm, ProfileUpdateForm
from django.contrib.auth import login


# Create your views here.
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.photo = request.FILES['photo']
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = Profile
    template_name = 'my_account.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user

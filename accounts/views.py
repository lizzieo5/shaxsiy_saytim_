from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")  # logout bo‘lgach qayerga yuboriladi

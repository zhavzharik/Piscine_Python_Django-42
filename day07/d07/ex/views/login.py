from ..forms.login import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy


class Login(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def get(self, request, *args: str, **kwargs):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You are already logged in!')
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: LoginForm):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            messages.error(self.request, "Invalid username or password!")
            return
        login(self.request, user)
        messages.info(self.request, f"You are now logged in as {username}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
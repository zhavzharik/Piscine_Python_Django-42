from typing import Optional
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from django.urls import reverse_lazy


class Logout(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_redirect_url(self, *args, **kwargs) -> Optional[str]:
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
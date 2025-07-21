from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import registroForm

class registroView(CreateView):
    model = User
    form_class = registroForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user:
            login(self.request, user)
            messages.success(self.request, f'Bienvenido {user.username}, tu cuenta fue creada correctamente.')
        return response

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

    def form_valid(self, form):
        messages.success(self.request, f'Hola {form.get_user().username}, has iniciado sesión correctamente.')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('inicio')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Has cerrado sesión correctamente.")
        return super().dispatch(request, *args, **kwargs)

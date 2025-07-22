from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from .forms import registroForm, UserForm, ProfileForm
from .models import Profile

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

class ProfileView(LoginRequiredMixin, View):
    template_name = 'usuarios/profile.html'

    def get(self, request):
        storage = messages.get_messages(request)
        list(storage)  
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })

    def post(self, request):
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)  # <-- MUY IMPORTANTE request.FILES para avatar

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('profile')

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form,
        })

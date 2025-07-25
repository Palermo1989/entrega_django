from django.urls import path
from .views import registroView, CustomLoginView, CustomLogoutView, ProfileView,datos_usuario_view


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registro/', registroView.as_view(), name='registro'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('datos/', datos_usuario_view, name='datos_usuario'),
    ]
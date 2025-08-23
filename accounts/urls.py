from django.urls import path
from django.contrib.auth.views import LogoutView , LoginView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', LoginView.as_view(next_page='home'), name='login'),
]
from django.urls import path
from AccountAPI.views import loginPost, RegisterView

urlpatterns = [
    path('login', loginPost, name='login'),
    path('signup', RegisterView.as_view(), name='signup')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllFAQs),
    path('add/', views.addFAQ),
    path('get/<int:id>/', views.getFAQById, name='get_FAQ_by_id'),
    path('delete/<int:id>/', views.deleteFAQ, name='delete_FAQ'),
    path('update/<int:id>/', views.updateFAQ, name='update_FAQ'),
]

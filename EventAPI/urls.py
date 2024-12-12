from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllEvents),
    path('add/', views.addEvent),
    path('get/<int:id>/', views.getEventById, name='get_event_by_id'),
    path('delete/<int:id>/', views.deleteEvent, name='delete_event'),
    path('update/<int:id>/', views.updateEvent, name='update_event'),
]

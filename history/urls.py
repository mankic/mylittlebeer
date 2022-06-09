from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.history_view, name='history'),
    path('history/delete/<int:id>', views.delete, name='delete'),
]

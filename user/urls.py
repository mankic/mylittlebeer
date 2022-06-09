from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('update-confirm/', views.update_confirm, name='update-confirm'),
    path('delete/', views.delete, name='delete'),
    path('delete-confirm/', views.delete_confirm, name='delete-confirm'),

]
# path('user/', views.user_view, name='user-list'),  # <- 여기에 컴마 주의!
# path('user_delete/', views.user_delete_view, name='user_delete'),
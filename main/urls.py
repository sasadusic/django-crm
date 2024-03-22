from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('records/', views.records, name='records'),
    path('record/<int:pk>/', views.record_details, name='record_details'),
    path('add_record', views.add_record, name='add_record'),
    path('edit_record/<int:pk>/', views.edit_record, name='edit_record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    path('profile/', views.profile, name='profile'),
]
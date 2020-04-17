from django.urls import path
from djangoapp import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('computer_entry',views.computer_entry,name = 'computer_entry'),
    path('computer_list',views.computer_list,name = 'computer_list'),
    path('update/<pk>',views.computer_list_update,name = 'computer_list_update'),
    path('delete/<pk>',views.computer_list_delete,name = 'computer_list_delete'),
    path('register',views.registration_view,name = 'register'),
    path('login',views.loginpage_view,name = 'login'),
    path('logout',views.logoutpage_view,name = 'logout'),
    path('computer_history_list',views.computer_history_list, name='computer_history_list'),
    path('historydelete/<id>',views.computer_history_list_delete, name='history_delete'),
]

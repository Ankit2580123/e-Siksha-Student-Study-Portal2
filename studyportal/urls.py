from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name="register"),
    path('userlist/',views.user_list,name='userlist'),
    path('del_user/<id>',views.delete_user,name='delete_user'),
    path('about/',views.about,name='about'),
    path('edit_user/<id>',views.editUser,name="editUser"),
    path('updateUser/',views.update_user,name='update_user'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('header/',views.header,name='header'),
    path('notes/', views.notes,name='notes'),
    path('homework/',views.homework,name='homework'),
    path('todo/',views.todo,name='todo'),
    path('calculator/',views.calculator,name="calculator"),
    # path('contact/',views.contact,name="contact"),
    # path('contact_details/',views.contact_details,name='contact_details'),
]
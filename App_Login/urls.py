from django.urls import path
from App_Login import views


app_name = 'App_Login'


urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='user_change'),
    path('password/', views.password_change, name='password_change'),
    path('add-picture/', views.add_profile_picture, name='add_profile_picture'),
    path('change-picture/', views.change_profile_picture, name='change_profile_picture'),

]





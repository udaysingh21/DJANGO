from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app' # set app_name to basic_app

urlpatterns = [
    path('', views.index, name='index'), # add index view to urlpatterns
    path('register/', views.register, name='register'), # add register view to urlpatterns
    path('login/', views.user_login, name='user_login'), # add user_login view to urlpatterns
    # path('special/', views.special, name='special'), # add special view to urlpatterns
    # path('logout/', views.user_logout, name='logout'), # add logout view to urlpatterns

]


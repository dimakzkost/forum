from rest_framework import routers
from django.urls import path, include
from users.views import UserViewSet, user_ok  # , login, logout, adduser, change_password
from django.contrib.auth import views as auth_views


app_name = 'users'

router = routers.DefaultRouter()
router.register(r'api/v1/users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('user_ok/<uuid:user_id>/<str:username>/', user_ok, name='user_ok'),
    # path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),
    # path('adduser/', adduser, name='adduser'),

    ]

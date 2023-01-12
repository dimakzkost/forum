from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from chat.views import mess_get, mess_patch, mess_del

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('get-mess/<uuid:user_id>/', mess_get, name='get_messages'),
    path('mess_patch/<uuid:mess_id>/', mess_patch, name='patch_messages'),
    path('mess_del/<uuid:mess_id>/', mess_del, name='del_messages'),
]

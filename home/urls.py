from django.urls import path
from .views import *


urlpatterns = [
    path('asset-tracking/',asset_tracking, name='asset_tracking'),
    path('dashboard-main/',dashboard_main, name='dashboard_main'),
    path('groups/',groups, name='groups'),
    path('integrations/',integrations, name='integrations'),
    path('members/',members, name='members'),
    path('reports/',reports, name='reports'),
    path('forgotpassword/',forgotpassword, name='forgotpassword'),
    path('registration/',registration, name='registration'),
    path('resetpassword/',resetpassword, name='resetpassword'),
    path('signin/',signin, name='signin'),
    path('signup/',signup, name='signup'),
]

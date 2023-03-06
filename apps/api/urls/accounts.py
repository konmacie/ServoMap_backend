from django.urls import path

from apps.api.views import accounts

# * parent url pattern: /api/accounts/
urlpatterns = [
    path('login/', accounts.LoginAPIView.as_view()),
    path('whoami/', accounts.WhoAmIAPIView.as_view()),
    path('logout/', accounts.logout),
    path('register/', accounts.CreateUserAPIView.as_view()),
    path('update/', accounts.UpdateUserAPIView.as_view()),
]

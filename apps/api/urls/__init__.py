from django.urls import path, include

urlpatterns = [
    path('locations/', include('apps.api.urls.locations')),
    path('custom-pins/', include('apps.api.urls.custompins')),
    path('accounts/', include('apps.api.urls.accounts')),
    path('report/', include('apps.api.urls.report')),
]

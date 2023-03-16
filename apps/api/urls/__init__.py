from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('locations/', include('apps.api.urls.locations')),
    path('custom-pins/', include('apps.api.urls.custompins')),
    path('accounts/', include('apps.api.urls.accounts')),
    path('report/', include('apps.api.urls.report')),
    path('reviews/', include('apps.api.urls.review')),
])

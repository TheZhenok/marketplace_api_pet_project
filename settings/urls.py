# Django
from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf import settings
from django.conf.urls.static import static

# DRF
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
] + static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

# ---------------------------------------
# Api-Endpoints
# 
router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)

urlpatterns += [
    path('',include(router.urls)),
]
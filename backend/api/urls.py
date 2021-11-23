from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from api.apps.users.views import UserViewSet, ProfileViewset
from api.apps.clients.views import LocationViewSet, ClientViewSet
from api.apps.services.views import ServiceViewSet



router = DefaultRouter()
router.register(r'auth/users/roles', UserViewSet)
router.register(r"auth/users/profiles", ProfileViewset)
router.register(r"clients", ClientViewSet)
router.register(r"locations", LocationViewSet)
router.register(r"services", ServiceViewSet)
#router.register(f"auth/", include("djoser.urls"))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include(router.urls)),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.authtoken")),
    # path("api/v1/auth/", include("djoser.urls.jwt")),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

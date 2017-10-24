from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from apps.users import views

from apps.tank import api as tank_api
from apps.users import api as users_api

router = DefaultRouter()

router.register('lists', tank_api.ListViewSet)
router.register('campaigns', tank_api.CampaignViewSet)
router.register('customers', tank_api.CustomerViewSet)
router.register('roles', users_api.RoleViewSet)
router.register('users', users_api.UserViewSet)

urlpatterns = [
    url(r'^stadmin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls, namespace='api')),
    url(r'^.*$', views.index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

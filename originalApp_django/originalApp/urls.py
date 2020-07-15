
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from needs.views import NeedViewSet
from user.views import UserViewSet
from master.views import OccupationViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('needs', NeedViewSet)
router.register('occupations', OccupationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('rest-auth/', include("rest_auth.urls")),
    path('rest-auth/registration/', include("rest_auth.registration.urls")),
]

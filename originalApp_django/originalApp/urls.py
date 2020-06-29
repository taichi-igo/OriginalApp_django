
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from needs.views import NeedViewSet
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('needs', NeedViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

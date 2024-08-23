from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
# from .views import upload_image

post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet)
urlpatterns = [
    path('api/', include(post_router.urls)),
]
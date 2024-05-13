from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.views import CategoryViewSet, CommentViewSet, PostViewSet, LikePostAPIView

app_name = "posts"

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"", PostViewSet)
router.register(r"^(?P<post_id>\d+)/comment", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("like/<int:pk>", LikePostAPIView.as_view(), name="like-post")
]

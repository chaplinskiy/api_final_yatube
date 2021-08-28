from django.urls import include, path

from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('v1/', include(router.urls,)),
    path('v1/', include('djoser.urls.jwt')),
]

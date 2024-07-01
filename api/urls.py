from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import EmailView, TokenView, UserProfileView, CategoriesView, GenresView, TitlesView, ReviewsView, CommentView 

router = DefaultRouter()

router.register(r'users', UserProfileView, basename='users')
router.register(r'users/<str:username>', UserProfileView, basename='users-me')
router.register(r'categories', CategoriesView, basename='categories')
router.register(r'genres', GenresView, basename='genres')
router.register(r'titles', TitlesView, basename='titles')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewsView, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentView, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenView.as_view(), name='auth-token'),
    path('auth/email/', EmailView.as_view(), name='auth-email'),
]
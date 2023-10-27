from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, PostCommentView,\
    PostCommentListCreateView, PostLikeListView, CommentRetrieveView

urlpatterns = [
    path('list/', PostListApiView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('<uuid:pk>/comments/', PostCommentView.as_view()),
    path('comments/', PostCommentListCreateView.as_view()),
    path('comments/<uuid:pk>/', CommentRetrieveView.as_view()),
    path('likes/<uuid:pk>/', PostLikeListView.as_view()),
]

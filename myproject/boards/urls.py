from . import views
from django.urls import path

urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('api/boards/', views.get_all_boards),
    path('api/boards/<int:pk>/', views.get_particular_board),
    path('api/boards/<int:pk>/topics/', views.get_all_topics_of_particular_board),
    path('api/boards/<int:board_pk>/topics/<int:pk>/', views.get_particular_topic),
    path('boards/<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('boards/<pk>/topics/<topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<pk>/topics/<topic_pk>/posts/<post_pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]

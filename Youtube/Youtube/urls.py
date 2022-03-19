
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from youtubeapp.views import PostViewSet,PostList,CommentViewSet,CommentList,VideoLista,VideoView,VideoList
from userapp.views import AccountView,AccountList

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Youtube clone API",
      default_version='v1',
      description="youtube clone versiyasi Django Rest Framework va Postgresqldan foydalangan",
      contact=openapi.Contact("Oyatillo Sharobiddinov <oyatillo0403317@gmail.com>,<+998900403317>"),
   ),
   public=True,
)

r=DefaultRouter()
r.register('post',PostViewSet)
r.register('comment',CommentViewSet)
r.register('account',AccountView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(r.urls)),
    path('post_list/',PostList.as_view()),
    path('comment_list/',CommentList.as_view()),
    path('video/',VideoList.as_view()),
    path('video_list/',VideoLista.as_view()),
    path('video_view/',VideoView.as_view()),
    path('account_list/',AccountList.as_view()),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),

]

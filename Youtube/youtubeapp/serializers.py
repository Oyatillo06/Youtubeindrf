from rest_framework.serializers import ModelSerializer

from .models import *



class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class VideoSerializers(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
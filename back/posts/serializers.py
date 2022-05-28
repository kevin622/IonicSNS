from rest_framework import serializers
from .models import Post, Comment, Image

class PostSerializer(serializers.Serializer):
    
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.Serializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class ImageSerializer(serializers.Serializer):
    
    class Meta:
        model = Image
        fields = '__all__'

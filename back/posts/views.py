from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Post, Comment, Image
from .serializers import CommentSerializer, PostSerializer

# Create your views here.
@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes(IsAuthenticated)
@api_view(['POST'])
def create_post(request):
    user = request.user
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(author=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes(IsAuthenticated)
@api_view(['PUT', 'DELETE'])
def change_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, pk=post_id)
    if user != post.author:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes(IsAuthenticated)
@api_view(['POST'])
def like_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, pk=post_id)
    if post.like_users.filter(pk=user.pk).exists():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_comments(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = get_list_or_404(Comment, post=post)
    serializer = CommentSerializer(comments)
    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes(IsAuthenticated)
@api_view(['POST'])
def create_comment(request, post_id):
    user = request.user
    post = get_object_or_404(Post, pk=post_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(author=user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes(IsAuthenticated)
@api_view(['PUT', 'DELETE'])
def change_comment(request, comment_id):
    user = request.user
    comment = get_object_or_404(Comment, pk=comment_id)
    if user != comment.author:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes(IsAuthenticated)
@api_view(['POST'])
def like_comment(request, comment_id):
    user = request.user
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.like_users.filter(pk=user.pk).exists():
        comment.like_users.remove(user)
    else:
        comment.like_users.add(user)
    return Response(status=status.HTTP_200_OK)
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer
User = get_user_model()

# Create your views here.
@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    me = request.user
    you = get_object_or_404(User, username=username)
    if me == you:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    if you.followers.filter(pk=me.pk).exists():
        # unfollow
        you.followers.remove(me)
    else:
        # follow
        you.followers.add(me)
    return Response(status=status.HTTP_200_OK)

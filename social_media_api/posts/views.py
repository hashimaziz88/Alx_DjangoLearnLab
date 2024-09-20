from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        return JsonResponse({'message': 'You have already liked this post.'})

    post.likes.add(request.user)
    Like.objects.create(post=post, user=request.user)

    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked',
        target=post
    )

    return JsonResponse({'message': 'Post liked.'})


def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user not in post.likes.all():
        return JsonResponse({'message': 'You haven’t liked this post yet.'})

    post.likes.remove(request.user)
    Like.objects.filter(post=post, user=request.user).delete()

    return JsonResponse({'message': 'Post unliked.'})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(author__in=following_users).order_by
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'content']
    search_fields = ['title', 'content']
    @action(detail=False, methods=['get'])
    def feed(self, request):
        user = request.user
        posts = Post.objects.filter(author__in=user.following.all()).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

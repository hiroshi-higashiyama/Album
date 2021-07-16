from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from .serializers import PostSerializer
from .models import Post


class PostPagination(PageNumberPagination):
    page_size = 8

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description', 'created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

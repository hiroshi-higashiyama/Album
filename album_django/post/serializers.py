from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "created_by",
            "description",
            "get_image",
            "get_thumbnail",
            "created_at",
            "updated_at",
        )

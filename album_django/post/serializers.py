from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = (
            "created_by",
            "updated_at",
        ),
        fields = (
            "id",
            "title",
            "description",
            "image",
            "thumbnail",
            "get_image",
            "get_thumbnail",
            "created_at",

        )

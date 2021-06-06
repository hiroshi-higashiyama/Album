from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = (
            "created_by",
            "created_at",
            "updated_at",
            "get_image",
            "get_thumbnail",
        ),
        fields = (
            "id",
            "title",
            "description",
            "image",

        )

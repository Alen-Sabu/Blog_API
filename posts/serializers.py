from rest_framework import serializers

from posts.models import Category, Comment, Post

class CategoryReadSerializer(serializers.ModelSerializer):
    """
    Serializer class to read the categories
    """
    class Meta:
        model = Category
        fields = "__all__"

class PostReadSerializer(serializers.ModelSerializer):
    """
    Serializer class to read the post
    """
    author = serializers.CharField(source = "author.username", read_only = True)
    categories = serializers.SerializerMethodField(read_only = True)
    likes = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_categories(self, obj):
        categories = list(
            cat.name for cat in obj.categories.get_queryset().only("name")
        )
        return categories
    
    def get_likes(self, obj):
        likes = list(
            like.username for like in obj.likes.get_queryset().only("username")
        )
        return likes
    
class PostWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class to create a post
    """
    author = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"

class CommentReadSerializer(serializers.ModelSerializer):
    """
    Serializezr class to read the comment
    """
    author = serializers.CharField(source = "author.username", read_only = True)

    class Meta:
        model = Comment
        fields = "__all__"

class CommentWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class to write the comment
    """
    author = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = "__all__"
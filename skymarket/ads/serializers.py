from rest_framework import serializers
from .models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    ad = serializers.SlugRelatedField(read_only=True, slug_field="title")
    author = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_first_name = serializers.SlugRelatedField(read_only=True, slug_field="author_first_name")
    author_last_name = serializers.SlugRelatedField(read_only=True, slug_field="author_last_name")
    author_id = serializers.CharField(source='author.id', read_only=True)
    author_image = serializers.CharField(source='author.image', read_only=True)
    ad_id = serializers.CharField(source='ad.id', read_only=True)

    class Meta:
        model = Comment
        #fields = ['id', 'ad', 'author', 'text', 'created_at', ]
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'



class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.CharField(source='author.id', read_only=True)

    # author_first_name = serializers.SerializerMethodField()
    # author_last_name = serializers.SerializerMethodField()
    # author_id = serializers.SerializerMethodField()
    #
    # def get_author_first_name(self, obj):
    #     return obj.author.first_name
    #
    # def get_author_last_name(self, obj):
    #     return obj.author.last_name
    #
    # def get_author_id(self, obj):
    #     return obj.author_id

    class Meta:
        model = Ad
        fields = '__all__'
from rest_framework import serializers
from api.models import User, Categories, Genres, Titles, Reviews, Comments
from django.shortcuts import get_object_or_404

class UserValidationMixin:

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError('Имя пользователя не может быть "me"')
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем уже существует')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Пользователь с таким email уже существует')
        return value

class EmailSerializer(serializers.Serializer, UserValidationMixin):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=6)

class UserSerializer(serializers.ModelSerializer, UserValidationMixin):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'role']
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'username': {'required': True, 'allow_blank': False}
        }

    def create(self, validated_data):
        return super().create(validated_data)

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'slug']

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['name', 'slug']

class TitleReadSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(read_only=True)
    genre = GenresSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True, required=False, default=None)
    class Meta:
        model = Titles
        fields = ['id', 'name', 'year', 'description', 'genre', 'category', 'rating']

class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', queryset=Categories.objects.all())
    genre = serializers.SlugRelatedField(slug_field='slug', queryset=Genres.objects.all(), many=True)
    class Meta:
        model = Titles
        fields = ['id', 'name', 'year', 'description', 'genre', 'category']

class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    title = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Reviews
        fields = ['id', 'text', 'author', 'score', 'pub_date', 'title']

    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка по 10-бальной шкале!')
        return value

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Titles, pk=title_id)
        if (
            request.method == 'POST'
            and Reviews.objects.filter(title=title, author=author).exists()
        ):
            raise serializers.ValidationError('Может существовать только один отзыв!')
        return data

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    review = serializers.SlugRelatedField(slug_field='text', read_only=True)
    class Meta:
        model = Comments
        fields = ['id', 'text', 'author', 'pub_date', 'review']
        read_only_fields = ('title',)
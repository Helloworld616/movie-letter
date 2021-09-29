from rest_framework import serializers
from .models import Genre, Movie, Review, Comment, Recommended


class RecommendedListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Recommended
        fields = '__all__'


class GenreSerilizers(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
        

class CommentListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)


class ReviewListSerializers(serializers.ModelSerializer):
    comment_set = CommentListSerializers(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)


class MovieSerializers(serializers.ModelSerializer):
    review_set = ReviewListSerializers(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
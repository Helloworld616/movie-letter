from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.title


class Recommended(models.Model):
    receiver_id = models.IntegerField() # 받는 사람의 pk 값을 저장
    review_title = models.CharField(max_length=100) # 편지(리뷰)의 제목을 저장
    review_content = models.TextField() # 편지(리뷰)의 내용을 저장
    review_rank = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)]) # 영화의 평점을 저장
    movie_id = models.IntegerField() # 영화의 pk 값을 저장
    movie_title = models.CharField(max_length=500) # 영화의 제목을 저장
    release_date = models.DateField() # 영화의 개봉일을 저장
    vote_count = models.IntegerField() # 영화에 평을 한 사람들의 수를 저장
    vote_average = models.FloatField() # 영화의 평점을 저장
    overview = models.TextField() # 영화의 줄거리를 저장
    poster_path = models.CharField(max_length=500) # 영화의 포스터 주소를 저장
    genres = models.ManyToManyField(Genre) # 영화의 장르를 저장

    def __str__(self):
        return self.title


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
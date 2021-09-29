from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator

from .models import Genre, Movie, Review, Comment, Recommended
from .serializers import (
    GenreSerilizers,
    MovieListSerializers,
    CommentListSerializers,
    ReviewListSerializers,
    MovieSerializers,
    RecommendedListSerializers
)
import requests

from random import randint


# 데이터 다운로드 함수
def download_genres():
    API_KEY = '1fd9c27d213a715cd8064276febb0396'
    URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR'
    genres = requests.get(URL).json().get('genres')

    for genre in genres:
        Genre.objects.create(
            id = genre.get('id'),
            name = genre.get('name')
        )


def download_movies():
    API_KEY = '1fd9c27d213a715cd8064276febb0396'

    for num in range(1, 35):
        URL = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko-KR&page={num}'
        movies = requests.get(URL).json().get('results')
        
        for movie in movies:
            if movie.get('overview'):
                movie_data = Movie.objects.create(
                                id = movie.get('id'),
                                title = movie.get('title'),
                                release_date = movie.get('release_date'),
                                vote_count = movie.get('vote_count'),
                                vote_average = movie.get('vote_average'),
                                overview = movie.get('overview'), 
                                poster_path = movie.get('poster_path'),
                            )
                for genre_id in movie.get('genre_ids'):
                    movie_data.genres.add(genre_id)


# 데이터 다운로드가 필요할 경우, 아래 두 코드 주석 해제하고 서버 실행
# download_genres()
# download_movies()


# view 함수
@api_view(['GET'])
def movie_all(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializers(movies, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    paginator = Paginator(movies, 12)
    
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)

    serializer = MovieListSerializers(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_genres(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerilizers(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    # 평점을 매긴 영화와, 편지를 작성한 유저 가져오기
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), username=request.user)

    # 시리얼라이저에 담을 데이터 정제
    context = request.data
    context['user'] = user.pk
    context['movie'] = movie.pk
    # 시리얼라이저에 담기
    serializer = ReviewListSerializers(data=context)

    # 나의 평점을, 영화의 평균 평점에 반영
    origin_count = movie.vote_count
    movie.vote_count += 1
    movie.vote_average = round((movie.vote_average * origin_count + context['rank']) / movie.vote_count, 1)
    movie.save() 

    # 사이트의 전체 유저 수 계산
    total_num = len(get_user_model().objects.all())

    # 편지를 보낼 유저 추첨
    if total_num == 1:
        receiver_id = 1
    else:
        while True:
            receiver_id = randint(1, total_num)
            if receiver_id != user.pk:
                break
    
    # 추첨 완료 후, Recommended Model에 필요한 정보 담기
    Recommended.objects.create(
        receiver_id = receiver_id,
        review_title = context['title'],
        review_content = context['content'],
        review_rank = context['rank'],
        movie_id = movie.pk,
        movie_title = movie.title,
        release_date = movie.release_date,
        vote_count = movie.vote_count,
        vote_average = movie.vote_average,
        overview = movie.overview, 
        poster_path = movie.poster_path,
    )

    # 시리얼라이저 유효성 검사 후 저장
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        serializer.save(user=user)
    
    # 시리얼라이저에 담긴 데이터를 응답으로 보내기
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_recommended(request):
    movies = get_list_or_404(Recommended)
    user = get_object_or_404(get_user_model(), username=request.user)
    recommended_movies = []
    for movie in movies:
        if movie.receiver_id == user.pk:
            recommended_movies.append(movie)

    serializer = RecommendedListSerializers(recommended_movies, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializers(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewListSerializers(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewListSerializers(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f"'{review.movie.title}'의 '{review.title}' 리뷰를 삭제했습니다."
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentListSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_list(request): 
    comments = get_list_or_404(Comment)
    serializer = CommentListSerializers(comments, many=True)
    return Response(serializer.data)
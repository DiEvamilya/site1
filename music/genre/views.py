from django.shortcuts import render, get_object_or_404

from django.shortcuts import render

from genre.models import Genre, Musician


def index_view(request):
    genres = Genre.objects.all()
    context = {'category': genres,
               'genre': 'genre'}
    return render(request, 'index.html', context=context)


def musician_list(request, genre_slug):
    genre = get_object_or_404(Genre, slug=genre_slug)
    musicians = Musician.objects.filter(genre=genre)
    context = {
        'genre': genre,
        'musicians': musicians
    }
    return render(request, 'musician_list.html', context)


def musician_detail_view(request, slug):
    musician = Musician.objects.get(slug=slug)
    context = {
        'musician': musician,
    }
    return render(request, 'musician_detail.html', context)





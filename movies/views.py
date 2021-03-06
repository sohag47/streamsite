from django.shortcuts import render,redirect,HttpResponse
from .models  import Allmovies,Moviesgenre,Tvepisodes,Tvgenre,Tvseries
from  .test_imdb import webscrapper
# Create your views here.
def home(request):
    context = {
        'movies':Allmovies.objects.filter().order_by('-id'),
         'lmovies':Allmovies.objects.filter().order_by('-id')[1:3],
         'fmovies':Allmovies.objects.filter().order_by('-id')[:1],
    }
    # context = {
    #     'movies':Movie.objects.filter().order_by('-id'),
    #     'lmovies':Movie.objects.filter().order_by('-id')[1:3],
    #      'fmovies':Movie.objects.filter().order_by('-id')[:1],
    #     'Genre':Genre.objects.all(),
    #     'Type':Type.objects.all()
    # }
    return render(request,'movies/home.html',context)




def video(request,id):
    movie  = Allmovies.objects.get(pk = id)
    
    # link1 = movie.moviehomepage
    
    # a=webscrapper(link1)
    # genres = a['genre']
    # genre =', '.join(genres)
    # sentence = a['stars']
    # star =", ".join(sentence)
    # print(a['video_length'])
    # context = {
    #     'movie':movie,
    #     'title': a['title'],
    #     'description':a['description'],
    #     'release_date':a['release_date'],
    #     'director':a['director'],
    #     'duration':a['video_length'],
    #     'stars':star,
    #     'genres':genre
    # }
    star  = movie.movieactors[:-1]
    content = {
        'movie':movie,
        'title':movie.movietitle,
        'description':movie.moviestory,
        'release_date':movie.movieyear,
        'moviecatagory':movie.moviecategory,
        'movierating':movie.movieratings,
        'stars':star,
        'moviegenre':movie.moviegenre
    }
    return render(request,'movies/video.html',content)

def search(request,id):
    movies = Allmovies.objects.filter(moviecategory= id).order_by('-id')
    # types = Type.objects.get(pk = id)     
    context = {
        'movies':movies,
        # 'types' :types
        
    }
    return  render(request,'movies/search.html',context)    



def searches(request,search):

    
     movies = Allmovies.objects.filter(movietitle__icontains=search) 
     context = {
         'movies':movies
     } 
     return render(request,'movies/searches.html',context) 
  
def movieurl(request):
    if request.method == 'POST':
        moviehomepage = request.POST['moviehomepage']
        saverecord = Allmovies()
        saverecord.moviehomepage = moviehomepage
        saverecord.save()
        return HttpResponse('')



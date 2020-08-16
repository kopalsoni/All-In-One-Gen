from django.shortcuts import render
from .gen_files import quotes, rand_images, music, createMaze


def home(request):
    quote_query = quotes.formatted_quote()
    return render(request, "home.html", {"data": quote_query})


def about(request):
    return render(request, "about.html")


def image_gen(request):
    rand_images.random_images()
    return render(request, "image_gen.html")


def music_gen(request):
    music.music_gen(1)
    return render(request, 'music_gen.html')


def maze_gen(request):
    createMaze.run(20, 20)
    return render(request, 'maze_gen.html')

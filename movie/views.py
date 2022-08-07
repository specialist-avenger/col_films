# from django.shortcuts import redirect, render
# from .models import Movie
# from .forms import MovieCreateForm
# from django.views.generic.edit import CreateView
# from moviepy.editor import *
# def create_film(request):
#     def convert(seconds):
#         hours = seconds // 3600
#         seconds %= 3600
#         mins = seconds // 60
#         seconds %= 60
#         return f'{mins}:{seconds}'

#     if request.method == 'POST':
#         form = MovieCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)# This allows us to insert the user as the uploader of the movie
#             obj.author = request.user
#             vid = request.FILES['movie']
#             clip = VideoFileClip(vid.temporary_file_path())
#             temp_length = int(clip.duration)
#             if temp_length > 600:
#                 length_error = 'Film Is Longer Than 15 Minutes'
#                 return render(request, 'add_film.html', {'form':form,'length_error':length_error})
#             elif temp_length <= 600:
#                 obj.length = convert(int(clip.duration))
#                 obj.save()
#                 return redirect('reg')
#     else:
#          form = MovieCreateForm()
#     return render(request, 'add_film.html', {'form':form})

# def list_film(request):

#     film = Movie.objects.all()
#     data = {
#         'film': film,
#     }
#     return render(request, 'list_film.html', data)
from django.shortcuts import render
from .models import Photo
# Create your views here.
def photo(request):
    photo = Photo.objects
    return render(request, 'photo/photo.html', {'photo' : photo})
    

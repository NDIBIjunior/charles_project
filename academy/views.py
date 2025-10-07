from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from .models import Formation, Video, Comment, Image
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    formations = Formation.objects.order_by('-created_at')[:6]
    videos = Video.objects.order_by('-created_at')[:6]
    return render(request, "academy/home.html", {"formations": formations, "videos": videos})

def formation_list(request):
    formations = Formation.objects.all().order_by('-created_at')
    return render(request, "academy/formations_list.html", {"formations": formations})

def formation_detail(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    # incrémentation du nombre de vue
    Formation.objects.filter(pk=formation.pk).update(views=F('views') + 1)
    formation.refresh_from_db(fields=['views'])
    comments = formation.comments.order_by('-created_at')
    comments_count = comments.count()
    
    return render(request, "academy/formation_detail.html", {"formation": formation, "comments": comments, "comments_count": comments_count})

def add_comment(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == "POST":
        autor = request.POST.get("autor") or "Anonyme"
        email = request.POST.get("email") or ""
        content = request.POST.get("content") or ""
        
        Comment.objects.create(
            formation=formation,
            autor=autor,
            email=email,
            content=content,
        )
    return redirect("academy:formation_detail", pk=formation.pk)

def video_list(request):
    videos = Video.objects.all().order_by('-created_at')
    return render(request, "academy/videos_list.html", {"videos": videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    Video.objects.filter(pk=video.pk).update(views=F('views') + 1)
    video.refresh_from_db(fields=['views'])
    return render(request, "academy/video_detail.html", {"video": video})

def gallery(request):
    images = Image.objects.all().order_by('-pk')
    return render(request, "academy/gallery.html", {"images": images})

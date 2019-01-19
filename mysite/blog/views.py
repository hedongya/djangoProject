from django.shortcuts import render
from blog.models import BlogsPost,IMG

# Create your views here.
def blog_index(request):
    blog_list=BlogsPost.objects.all()
    return render(request,'index.html',{'blog_list':blog_list})
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
    return render(request, 'uploadimg.html')

def showImg(request):
    imgs = IMG.objects.all(),
    return render(request, 'index.html', {'imgs':imgs})

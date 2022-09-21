from ngopikuy.models import Post
from django.views import generic
from django.shortcuts import render, redirect
from ngopikuy.forms import PostForm  
from django.shortcuts import get_object_or_404
from django.contrib import messages
from ngopikuy.controllers.decorators import  employee_only, admin_only

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'page/blogs/post_detail.html'

def PostList(request):
    posting = Post.objects.all()
    context = {'posting':posting}
    return render (request, 'page/blogs/blogs.html',context)

def AddPostView(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New post created!")
    form = PostForm()
    return render(request, 'page/blogs/add_post.html', {'form':form})

def EditPost(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(instance=instance)
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Post edited!")

    return render(request, 'page/blogs/edit_post.html', {'form':form})

@employee_only
def BlogListPage(request):
    blogs = Post.objects.all()
    context = {'blogs': blogs}
    return render (request, 'page/blogs/blogs_list.html',context)

@admin_only
def DeletePost(request, pk):
    Post.objects.get(slug=pk).delete()
    messages.success(request, 'Post Deleted')
    return redirect('bloglist')
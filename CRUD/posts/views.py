from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_list(request):
    # return HttpResponse('글 리스트')
    '''
    Read(R)
    포스트들을 불러와서 리스트 형태로 보여준다
    '''
    posts = Post.objects.all()
    ctx = {'posts': posts}  # dictionary

    return render(request, template_name='posts/list.html', context=ctx)


def post_detail(request, post_id):
    '''
    Read(R)
    특정 포스트를 불러와서 상세정보를 보여준다
    '''
    post = Post.objects.get(id=post_id)
    ctx = {'post': post}

    return render(request, 'post/detail.html', context=ctx)

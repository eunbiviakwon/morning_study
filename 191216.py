from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from blog.models import Post

def post_list(request):
    # Template을 찾을 경로에서
    #  post_list.html을 찾아서
    # 그 파일을 text로 만들어서 HttpResponse 형태로 돌려준다
    # 위 기능을 하는 shortcut 함수

    # contents = loader.render_to_string('post_list.html', None, request)
    # return HttpResponse(content)

    # 1. posts라는 변수에 전체 Post를 가지는 QuerySet 객체를 할당
    #   hint) Post.objects.무언가... 를 실행한 결과는 QuerySet 객체가 된다.
    # 2. context라는 dict를 생성하며, 'posts'키에 위 posts변수를 value로 사용하도록 한다.
    # 3. render의 3번째 위치인자로 위 context변수를 전달한다.
    posts = Post.objects.order_bu('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    print('post_detail request', request)
    print('post_detail pk', pk)

    # URL: /post-detail/
    # View: post_detail ( 이 함수)
    # Template: post_detail.html
    # 내용으로 <h1>Post Detail!</h1> 을 갖도록 함

    # 1. 전체 Post 목록



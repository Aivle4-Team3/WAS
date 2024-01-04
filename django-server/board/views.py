from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from math import ceil
from .models import *
from .forms import *
# Create your views here.


# 전체 목록 보기
def board(request):
    search_key = request.GET.get('q','')
    post_list = Post.objects.filter(title__contains=search_key)
    post_list = post_list.order_by('-id')

    page = int(request.GET.get('page', 1))
    per = int(request.GET.get('per', 10))
    total = len(post_list)
    last = ceil(total/per)
    board_list = range(1, last+1)
    per_list = [7, 10, 20, 50]

    start = per*(page-1)
    end = per*page

    return render(request, 'board/board.html', {
        'post_all': post_list[start:end], 'q': search_key, 'page': page, 'per': per,
        'board_list': board_list, 'per_list': per_list, 'total': total, 'last': last})


# 상세 보기
def detail(request, no):
    post = get_object_or_404(Post, id=no)  # 인스턴스
    comment_list = post.comments.all()  # QuerySet
    tag_list = post.tag.all()  # QuerySet

    comment_form = CommentForm()
    return render(request, 'board/detail.html', {'post': post, 'comment_all': comment_list, 'tag_list': tag_list, 'comment_form': comment_form})


def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print('cleaned_data:', form.cleaned_data)
            # DB에 추가
            # post = Post.objects.create(**form.cleaned_data)
            # 모델 인스턴스만 만들어지고 저장은 안 됨: commit=False
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # get_absolute_url이 POST에서 자동으로 실행: return은 HttpResponse
            return redirect(post)
    else:
        form = PostModelForm()

    return render(request, 'board/post_form.html', {'form': form})


# Form 기반 Data 수정
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # 추가도 하고 수정도 가능, 구분은 새로운 데이터면 추가 디비에서 가져온거면 수정
            return redirect('board:list')
    else:
        form = PostModelForm(instance=post)

    return render(request, 'board/post_update.html', {'form': form})


# Data 삭제 작업
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('board:list')
    else:
        return render(request, 'board/post_delete.html', {'post': post})


def create_comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, id=id)
            comment.author = request.user
            comment.save()
            return redirect('board:detail', id)


def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.author == comment.author:
        comment.delete()
    return redirect('board:detail')

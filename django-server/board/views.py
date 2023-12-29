from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def board(request):
    post_list = Post.objects.all().order_by('-id')
    search_key = request.GET.get('keyword')
    if search_key:
        post_list=Post.objects.filter(title__contains=search_key)
    return render(request, 'board/board.html', {'post_all' : post_list, 'q':search_key})


# Create your views here.
# 뷰 객체 : 서비스 처리 객체
def test1(request):
    # 서비스 구현
    
    return HttpResponse('hello') # 200 ok

def test2(requset, no):
    print(type(no))
    return HttpResponse(no)

# 전체 목록 보기
def list(request):
    post_list = Post.objects.all()
    search_key = request.GET.get('keyword')
    if search_key:
        post_list=Post.objects.filter(title__contains=search_key)
    # return HttpResponse(post_all)
    return render(request, 'board/board.html', {'post_all' : post_list, 'q':search_key}) # 템플릿을 응답하고 싶을 때 사용

# 상세 보기
def detail(request, no):
    # post = Post.objects.get(id=no)
    post = get_object_or_404(Post, id=no) # 인스턴스
    comment_list = post.comments.all() # QuerySet
    tag_list = post.tag.all() # QuerySet
    # return HttpResponse(post.title)
    comment_form=CommentForm()
    return render(request, 'board/detail.html', {'post' : post, 'comment_all':comment_list, 'tag_list':tag_list, 'comment_form':comment_form})

def profile(request):
    user = User.objects.first()
    return render(request, 'board/profile.html', {'user' : user})

def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'board/list.html', {'post_all' : post_list})

def test3(request):
    print('요청 방식:',request.method)
    print('Get방식으로 전달된 문자열:', request.GET)
    print('Post방식으로 전달된 문자열:', request.POST)
    return render(request, 'board/form_test.html')

def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print('cleaned_data:', form.cleaned_data)
            # DB에 추가
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save(commit=False) # 모델 인스턴스만 만들어지고 save는 안된다 : commit=False
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post) # get_absolute_url이 POST에서 자동으로 실행 : return은 HttpResponse
    else:
        form = PostModelForm()
    
    return render(request, 'board/post_form.html', {'form':form})

# Form 기반 Data 수정
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save() # 추가도 하고 수정도 가능, 구분은 새로운 데이터면 추가 디비에서 가져온거면 수정 
            return redirect('board:list')
    else:
        form = PostModelForm(instance=post)
    
    return render(request, 'board/post_update.html', {'form':form})

# Data 삭제 작업
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method=='POST':
        post.delete()
        return redirect('board:list')
    else:
        return render(request, 'board/post_delete.html', {'post':post})
    
def create_comment(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = '익명'
        comment.save()
    return redirect('board:detail', post.id)

def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.author == comment.author:
        comment.delete()
    return redirect('board:detail')
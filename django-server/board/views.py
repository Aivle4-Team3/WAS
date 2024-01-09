from django.shortcuts import render, get_object_or_404, redirect
from math import ceil
from .models import *
from .forms import *
# Create your views here.


class Which:
    def __init__(self, BoardModel, BoardModelForm, app_name):
        self.BoardModel = BoardModel
        self.BoardModelForm = BoardModelForm
        self.app_name = app_name

    # 전체 목록 보기
    def board(self, request):
        search_key = request.GET.get('q', '')
        post_list = self.BoardModel.objects.filter(title__contains=search_key)
        post_list = post_list.order_by('-id')
        for post in post_list:
            post.category = post.__class__.__name__

        page = int(request.GET.get('page', 1))
        per = int(request.GET.get('per', 10))
        total = len(post_list)
        last = ceil(total/per)
        board_list = range(1, last+1)
        per_list = [7, 10, 20, 50]

        start = per*(page-1)
        end = per*page

        return render(request, 'board/board.html', {
            'namespace': self.app_name,
            'post_all': post_list[start:end], 'q': search_key, 'page': page, 'per': per,
            'board_list': board_list, 'per_list': per_list, 'total': total, 'last': last})

    # 상세 보기

    def detail(self, request, no):
        post = get_object_or_404(self.BoardModel, id=no)  # 인스턴스
        comment_list = post.comments.all()  # QuerySet
        tag_list = post.tag.all()  # QuerySet

        comment_form = CommentForm()
        return render(request, 'board/detail.html', {
            'namespace': self.app_name,
            'post': post, 'comment_all': comment_list, 'tag_list': tag_list, 'comment_form': comment_form})

    def post_create(self, request):
        if request.method == 'POST':
            form = self.BoardModelForm(request.POST)
            if form.is_valid():
                # DB에 추가
                # post = self.BoardModel.objects.create(**form.cleaned_data)
                # 모델 인스턴스만 만들어지고 저장은 안 됨: commit=False
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                # get_absolute_url이 POST에서 자동으로 실행: return은 HttpResponse
                return redirect(post)
        else:
            form = self.BoardModelForm()

        return render(request, 'board/post_form.html', {'namespace': self.app_name, 'form': form})

    # Form 기반 Data 수정

    def post_update(self, request, id):
        post = get_object_or_404(self.BoardModel, id=id)
        if request.method == 'POST':
            form = self.BoardModelForm(request.POST, instance=post)
            if form.is_valid():
                form.save()  # 추가도 하고 수정도 가능, 구분은 새로운 데이터면 추가 디비에서 가져온거면 수정
                return redirect('board:detail', id)
        else:
            form = self.BoardModelForm(instance=post)

        return render(request, 'board/post_form.html', {'namespace': self.app_name, 'form': form})

    # Data 삭제 작업

    def post_delete(self, request, id):
        post = get_object_or_404(self.BoardModel, id=id)
        post.delete()
        return redirect('board:board')
    
    def create_comment(self, request, id):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = get_object_or_404(self.BoardModel, id=id)
                comment.author = request.user
                comment.save()
                return redirect('board:detail', id)

    def delete_comment(self, request, id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('board:detail', id)

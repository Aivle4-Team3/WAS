from django.db import models
from django.urls import reverse
from accounts.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()
    tag = models.ManyToManyField('Tag', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    # null=True: 기존에 있던 데이터의 값들은 null
    # blank=True: Tag 데이터를 선택하지 않아도 저장됨
    # ManyToManyField는 모델명을 ''(str)에 넣어서 선언: 다이렉트로 선언되는 게 아니기 때문에

    def __str__(self):
        return self.title  # 모델 인스턴스를 출력했을 때 원하는 값으로 재정의, 여기서는 title로 출력

    def get_absolute_url(self):  # redirect에 모델 인스턴스를 줬을 때 이 함수가 자동으로 실행됌
        # url 생성 : /blog/id/, "앱 이름: path_name"
        return reverse("board:detail", args=[self.id])


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

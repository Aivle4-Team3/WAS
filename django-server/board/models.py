from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model): # 
    title = models.CharField(max_length=250) # 글자수를 정해야 됌
    body = models.TextField() # 글자수 상관없음
    ip = models.GenericIPAddressField(null=True) # 기존의 데이터의 ip값들은 null로 하겠다
    tag = models.ManyToManyField('Tag', null=True, blank=True) 
    # null=True : 기존에 있던 데이터 값들은 null, blank=True : Tag데이터를 선택 안해도 save 된다.
    # ManyToManyField는 모델명을 ''(str) 에 넣어서 선언해야 한다. : 다이렉트로 선언 되는 게 아니기 때문에
    
    def __str__(self):
        return self.title # 모델 인스턴스를 출력했을 때 원하는 값으로 재정의, 여기서는 title로 출력
    
    def get_absolute_url(self): # redirect에 모델 인스턴스를 줬을 때 이 함수가 자동으로 실행됌
        return reverse("board:detail", args=[self.id]) # url 생성 : /blog/id/,  "앱이름:path_name"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    

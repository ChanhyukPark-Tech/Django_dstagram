from django.db import models

# Create your models here.


# 1. 모델 : 데이터베이스 저장될 데이터가 있으면 해당 데이터를 묘사한다.
# 2. 뷰(기능) : 계산 , 처리 - 실제 기능, 화면 
# 3. URL 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록 - 주소 지정  해당 뷰를 어떤주소로접속하면 동작하게 할것이다 
# 4. 화면에 보여줄 것이있다 : 템플릿작성(html)

# 장고의 기본 유저 모델
from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):          # models.Model 에 장고의 별도 데이터베이스 기능들이 다 구현되어있다 . class 상속 만세 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',default = 'photos/no_image.png') # 업로드를 어디다할껀데?
    text = models.TextField() # 기본값이 없어도 들어간다 아무내용없어도 들어간다 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
      # makemigrations => migrate # 데이터베이스에 반영
    class Meta:
        ordering = ['-updated']       # 제일최근에 쓰여진 사진이 제일먼저 나오게되어있다. , 찍고여러가지기준 정할 수있 다
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")   # 사진을 작성한 유저의 아이디까지 알아낼 수 있따 search 그런것도 구현가능
    def get_absolute_url(self):
        return reverse('photo:photo_detail',args=[self.id])


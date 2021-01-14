from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    writer = models.CharField(verbose_name='글쓴이', max_length=50)
    content = models.TextField(verbose_name='내용')
    # DB에는 없는 ORM이라고 함(생성과 업데이트 시각 기록)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # string으로 title 반환
    def __str__(self):
        return self.title

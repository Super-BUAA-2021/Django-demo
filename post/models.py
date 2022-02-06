from django.db import models

# Create your models here.

class Post(models.Model):
	id = models.AutoField(primary_key=True)
	# 主键
	uid = models.IntegerField()
	# 发表该博客的用户id
	# 也可以选择用外键连接到User表中
	title = models.CharField(max_length=50)
	# 博客标题
	article = models.TextField(null=True, blank=True)
	# 博客正文
	# 因为可能很长，所以使用 TextField 字段
	time = models.DateTimeField()
	# 发表时间

	def to_dic(self):
		return {
			'id': self.id,
			'title': self.title,
			'time': self.time,
			'article': self.article,
			'uid': self.uid
		}
from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
	user_id = models.BigAutoField(primary_key = True)
	username = models.CharField(max_length = 15)
	first_name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 150)
	password = models.CharField(max_length=30)


class Likes(models.Model):
	pass

class Post(models.Model):
	post_id = models.BigAutoField(primary_key = True)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 50)
	date = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	#username = models.CharField(max_length=30)
	#comment_id = models.ForeignKey(Comment, on_delete = models.CASCADE)
	like_id = models.ForeignKey(Likes, on_delete = models.CASCADE)
    
    
	def str(self):
	    return self.title


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField(max_length=2500)
    date = models.DateTimeField()

    def str(self):
        return self.username






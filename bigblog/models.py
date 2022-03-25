
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Likes(models.Model):
	pass

class Post(models.Model):
	STATUS_CHOICES = (
		("draft", "Draft"),
		("published", "Published"),
	) 
	title = models.CharField(max_length = 50)
	slug = models.SlugField(max_length = 250, unique=True, null=True)
	author = models.ForeignKey(User, on_delete = models.CASCADE,  related_name = "blog_posts")
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = "draft")


	def get_absolute_url(self):
		return reverse('bigblog:post_detail', args =[self.publish.year,self.publish.strftime('%m') ,self.publish.strftime('%d'),self.slug])
		
	class Meta:
		ordering: ('-publish',)

	def __str__(self):
		return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)




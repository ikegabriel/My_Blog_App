from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=(str(self.id)))

CATEGORIES = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in CATEGORIES:
    choice_list.append(item)


class Posts(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(upload_to='images/%y%m%d',null=True, blank=True, default='static/blog/images/default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.TextField(max_length=255, choices=CATEGORIES, default='business')
    title_tag = models.CharField(max_length=200, null=True)
    article = RichTextField(blank=True, null=True)
    article_snippet = models.CharField(max_length=500, null=True)
    update_date = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    favourites = models.ManyToManyField(User, related_name='blog_favourites')
    def total_likes(self):
        return self.likes.count()

    
    def __str__(self):
        return self.title + ' By ' + str(self.author)

    def get_absolute_url(self):
        return reverse('detail', args=(self.id,))

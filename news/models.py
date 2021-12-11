from django.db import models

from team.models import Employee

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=100, help_text="Enter title")
    news_text = models.TextField(max_length=10000, help_text="Enter text")
    creation_date = models.DateTimeField(auto_now_add=True)
    updating_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    likes = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return f"{self.title} - {self.news_text[:40]}"


class Comment(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(Employee, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    updating_date = models.DateTimeField(auto_now=True)



from django.db import models
from django.contrib.auth.models import AbstractUser

import question_box


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"


class Question(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    favorited_by = models.ManyToManyField(User, related_name='favorite_questions', blank=True)

    def __str__(self):
        return self.title

class Answer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answered_question')
    description = models.CharField(max_length=500)
    favorited_by = models.ManyToManyField(User, related_name='favorite_answers', blank=True)

    def __str__(self):
        return self.description

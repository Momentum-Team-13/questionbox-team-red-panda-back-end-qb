from django.db import models
from django.contrib.auth.models import AbstractUser
from django_toggle_m2m.toggle import ToggleManyToMany


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


class Category(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Game(models.Model):
    game = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='game_category')

    def __str__(self):
        return self.game


class Question(BaseModel, ToggleManyToMany):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    favorited_by = models.ManyToManyField(User, related_name='favorite_questions', blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='games', null=True)

    TOGGLEABLE_FIELDS = ('favorited_by')

    def __str__(self):
        return self.title


class Answer(BaseModel, ToggleManyToMany):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answered_question')
    description = models.CharField(max_length=500)
    favorited_by = models.ManyToManyField(User, related_name='favorite_answers', blank=True)

    TOGGLEABLE_FIELDS = ('favorited_by')

    def __str__(self):
        return self.description

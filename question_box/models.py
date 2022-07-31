from django.db import models
from django.contrib.auth.models import AbstractUser


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


class Game(models.Model):
    ACTION_GAME = 'Action'
    FIGHTING_GAME = 'Fighting'
    ADVENTURE_GAME = 'Adventure'
    IDLE_GAME = 'Idle'
    PUZZLE_GAME = 'Puzzle'
    RACING_GAME = 'Racing'
    ROLE_PLAYING_GAME = 'Role-Playing'
    SIMULATION_GAME = 'Simulation'
    SPORTS_GAME = 'Sports'
    STRATEGY_GAME = 'Strategy'

    QUESTION_CATEGORIES = [
        (ACTION_GAME, 'Action Game'),
        (FIGHTING_GAME, 'Fighting Game'),
        (ADVENTURE_GAME, 'Adventure Game'),
        (IDLE_GAME, 'Idle Game'),
        (PUZZLE_GAME, 'Puzzle Game'),
        (RACING_GAME, 'Racing Game'),
        (ROLE_PLAYING_GAME, 'Playing Game'),
        (SIMULATION_GAME, 'Simulation Game'),
        (SPORTS_GAME, 'Sports Game'),
        (STRATEGY_GAME, 'Strategy Game'),
    ]

    game = models.CharField(max_length=80)
    category = models.CharField(max_length=12, choices=QUESTION_CATEGORIES)

    def __str__(self):
        return self.game


class Question(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    favorited_by = models.ManyToManyField(User, related_name='favorite_questions', blank=True)
    game = models.ManyToManyField(Game, related_name='games', blank=True)

    def __str__(self):
        return self.title


class Answer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answered_question')
    description = models.CharField(max_length=500)
    favorited_by = models.ManyToManyField(User, related_name='favorite_answers', blank=True)

    def __str__(self):
        return self.description

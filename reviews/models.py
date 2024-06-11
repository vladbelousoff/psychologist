from django.db import models


class Review(models.Model):
    review_text = models.TextField()
    author_name = models.CharField(max_length=100)
    pub_date = models.DateField("Date published")

    def __str__(self):
        return f"{self.author_name} - {self.review_text}"


class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()

    def __str__(self):
        return f"{self.question_text}"

from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Review(models.Model):
    review_text = models.TextField()
    author_name = models.CharField(max_length=100)
    pub_date = models.DateField("Date published")

    def __str__(self):
        return f"{self.author_name} - {self.review_text}"


class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.question_text}"

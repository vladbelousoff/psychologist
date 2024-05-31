from django.db import models


class Review(models.Model):
    review_text = models.TextField()
    author_name = models.CharField(max_length=100)
    pub_date = models.DateField("Date published")

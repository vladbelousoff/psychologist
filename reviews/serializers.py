from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from reviews.models import Review, Question, Language


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    language = ReadOnlyField(source='language.name')

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answer_text', 'language']

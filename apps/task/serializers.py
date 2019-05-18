from rest_framework import serializers

from apps.comment.models import Comment
from apps.task.models import Task
from rest_framework.exceptions import ValidationError


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "description", "status", "user_created")


# --------Comments
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'text']


class DetailTaskSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = Comment.objects.filter(task=obj.id)
        return CommentsSerializer(comments, many=True).data

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'comments']


# class FilterTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('status', 'user_assigned', 'title')


class MyFilterSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=False)
    status = serializers.CharField(max_length=10, required=False)
    user_assigned = serializers.IntegerField(required=False)

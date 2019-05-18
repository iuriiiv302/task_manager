from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.comment.models import Comment
from rest_framework.response import Response
from apps.comment.serializers import CommentSerializer
from apps.notification.views import AddNotificationComment

# task 10
class AddCommentView(GenericAPIView):
    serializer_class = CommentSerializer

    permission_classes = (IsAuthenticated,)

    @serialize_decorator(CommentSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comment = Comment.objects.create(
            task=validated_data['task'],
            user=request.user,
            text=validated_data['text'],
        )
        comment.save()

        AddNotificationComment(comment.user, comment)

        return Response(CommentSerializer(comment).data)

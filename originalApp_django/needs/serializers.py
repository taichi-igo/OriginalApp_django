from rest_framework import serializers
from needs.models import Need#, Comment
from user.serializers import UserSerializer

class NeedSerializer(serializers.ModelSerializer):
# ニーズのシリアライザ（一覧用）
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Need
        # fields = '__all__'
        fields = (
            'id',
            'user_id',
            'occupation_id',
            'content',
            'username',
            'created_at',
        )

# class CommentSerializer(serializers.ModelSerializer):
# # コメントのシリアライザ
#     class Meta:
#         model = Comment
#         # fields = '__all__'
#         fields = (
#             'id',
#             'content',
#             'user_id',
#         )

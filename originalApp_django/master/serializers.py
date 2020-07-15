from rest_framework import serializers
from master.models import Occupation#, Comment
from user.serializers import UserSerializer

class OccupationSerializer(serializers.ModelSerializer):
    """ 業種のシリアライザ（一覧用）"""

    class Meta:
        model = Occupation
        fields = '__all__'

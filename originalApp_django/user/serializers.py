from rest_framework import serializers
from user.models import User
from rest_framework.fields import SerializerMethodField

class UserSerializer(serializers.ModelSerializer):

    age = SerializerMethodField()

    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            'id',
            'username',
            'age',
        )

    def get_age(self, obj):
        if obj.age < 0:
            return ''

        else :
            return f'{obj.age}歳'

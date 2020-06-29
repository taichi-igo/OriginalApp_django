from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from datetime import datetime

from user.models import User
from user.serializers import UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from master.models import Occupation
from copy import copy

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializers_class = UserSerializer

    # users/ GET
    def list(self, request):
        query = User.objects.all()
        # query = User.objects.filter(deleted=False)
        data = UserSerializer(query, many=True).data
        return Response(data)

    # users/ POST
    def create(self, request):

        # post_data = copy(request.data)
        post_data = request.data.copy()
        occupation_id = post_data.get('occupation_id')
        del post_data['occupation_id']
        occupation = Occupation.objects.get(id=occupation_id)

        try :
            user = User.objects.create(occupation_id=occupation, **post_data)
            data = UserSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)

        except Exception as error :
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)





# Create your views here.

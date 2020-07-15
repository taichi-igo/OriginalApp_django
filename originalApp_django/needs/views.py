from datetime import datetime
from copy import copy

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from needs.models import Need#, Comment
from needs.serializers import NeedSerializer#, CommentSerializer
from django.contrib.auth.models import AnonymousUser
from master.models import Occupation
from user.serializers import UserSerializer

class NeedViewSet(viewsets.ModelViewSet):
    queryset = Need.objects.all()
    serializers_class = NeedSerializer

    # needs/ GET
    def list(self, request):
        occupation = request.GET.get("occupation", "")
        query = self.queryset.filter(
            occupation_id__name = occupation,
            is_passed = True
        )
        data = self.serializers_class(query, many=True).data
        return Response(data)

    # needs/ POST
    def create(self, request):
        # try :
        # print(request.user)
        # print(type(request.user))
        # ログインしてない場合

        if type(request.user)==AnonymousUser:
            occupation_id = request.data.get('occupation_id')
            occupation = Occupation.objects.get(id=occupation_id)
            user = User.objects.get(id=1)
            username = request.data.get('username')


        # ログインしている場合
        else :
            user = request.user# User.objects.get()
            occupation = user.occunpation_id
            username = user.username

        content = request.data.get('content')
        need = Need.objects.create(
            username=username,
            user_id=user,
            occupation_id=occupation,
            content=content,
        )
        serializer = NeedSerializer(need)
        return Response(serializer.data)




    # needs/:id/comments/  POST
    # @action(methods=['post'], detail=True)
    # def comment(self, request, pk=None):
    #     me = request.user
    #     need = Need.objects.get(id=pk)#.order_by('created_at')
    #     comment = Comment.objects.create(
    #             need_id=need,
    #             user_id=me,
    #             text=request.data.get('text'),
    #     )
    #     data = CommentSerializer(comment).data
    #     return Response(data)


# Create your views here.

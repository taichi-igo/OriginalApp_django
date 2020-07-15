from rest_framework import viewsets
from rest_framework.response import Response

from master.models import Occupation#, Comment
from master.serializers import OccupationSerializer#, CommentSerializer

class OccupationViewSet(viewsets.ModelViewSet):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer

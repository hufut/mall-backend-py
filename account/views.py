from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets
from account.serializers import UserSerializer, GroupSerializer

def health_check(request):
    """
    ok kkkkk
    :param request:
    :return:
    """
    # health check response for tengine
    return HttpResponse('love you')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

from django.db.models import Q
from rest_framework import generics, mixins
from ngo_requirements.models import *
from .serializers import RequirementSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'RequirementList':'/requirementlist/',
		'Detail Requirement List':'/requirementlist/<str:username>/',
		}

	return Response(api_urls) 

class NgoRequirementList(generics.ListAPIView):
    serializer_class = RequirementSerializer
    # queryset = Complain.objects.all()
    def get_queryset(self):
        username = self.kwargs.get('username')
        if User.objects.filter(username = username).exists():
            user =  User.objects.get(username = username)
            ngo = Ngo.objects.get(user = user)
        return Requirement.objects.filter(ngo = ngo)

class RequirementList(generics.ListAPIView):
    serializer_class = RequirementSerializer

    def get_queryset(self):
        return Requirement.objects.all()

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

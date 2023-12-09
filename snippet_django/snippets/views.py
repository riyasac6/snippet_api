# from rest_framework import generics

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer

# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    # API to return snippets linked to the selected tag.
    @action(detail=True, methods=['get'])
    def snippets(self, request, pk=None):
        tag = self.get_object()
        snippets = Snippet.objects.filter(tag=tag)
        serializer = SnippetSerializer(snippets, many=True, context = {'request': request})
        return Response(serializer.data)

class OverviewAPI(APIView):
    def get(self, request):
        snippet_count = Snippet.objects.count()
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True, context = {'request': request})
        data = {
            'total_count': snippet_count,
            'snippets': serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)


from rest_framework import serializers
from .models import Tag, Snippet

class TagSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Tag
		fields = ['url', 'id', 'title']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Snippet
		fields = ['url', 'id', 'title', 'content', 'timestamp', 'user', 'tag']
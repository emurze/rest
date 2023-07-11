from django.utils import timezone
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Women
        fields = '__all__'

    def delete(self):
        self.instance.delete()
        return self.instance

# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     created = serializers.DateTimeField(default=timezone.now)
#     updated = serializers.DateTimeField(default=timezone.now)
#     published = serializers.BooleanField(default=True)
#
#     def create(self, validated_data):
#         instance = Women.objects.create(**validated_data)
#         return instance
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created = validated_data.get('created', instance.created)
#         instance.updated = validated_data.get('updated', instance.updated)
#         instance.published = validated_data.get('published',
#                                                 instance.published)
#         instance.save()
#         return instance
#
#     def delete(self):
#         self.instance.delete()
#         return self.instance

from rest_framework import serializers

from django.contrib.auth.models import User


class bloggerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =User
        
        fields =(
            'username',
            'is_superuser',
            'url',
            'email',
            'id'

        )
 
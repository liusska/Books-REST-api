from rest_framework import serializers
from .models import BookModel


class BookSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['title']:
            if not data['title'][0].isupper():
                raise serializers.ValidationError("Must start with capital")
        return data

    class Meta:
        model = BookModel
        fields = '__all__'
